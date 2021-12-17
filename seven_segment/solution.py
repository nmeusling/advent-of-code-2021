from utils import read_file_lines


def get_input():
    input_lines = read_file_lines("input.txt")
    all_output = []
    all_signals = []
    for line in input_lines:
        signals, output = line.split("|")
        signals = signals.split()
        all_signals.append(signals)
        output = output.split()
        all_output.append(output)
    return all_signals, all_output


def get_output(signals, encoded_output):
    decoder = get_decoder(signals)
    decoded_output = [decoder["".join(sorted(output))] for output in encoded_output]
    output = [str(x) for x in decoded_output]
    return int("".join(output))


def sum_all_output(all_signals, all_output):
    sum = 0
    for signal, output in zip(all_signals, all_output):
        sum += get_output(signal, output)
    return sum


def encode_signals(signals):
    # signals has the 10 signals
    encoder = {}
    signals_by_length = get_signals_by_length(signals)
    encoder[1] = set(signals_by_length[2].pop(0))
    encoder[4] = set(signals_by_length[4].pop(0))
    encoder[7] = set(signals_by_length[3].pop(0))
    encoder[8] = set(signals_by_length[7].pop(0))
    encoder[6] = get_signals_from_list_that_have_x_matches_with_signal(signals_by_length[6], encoder[7], 2)
    encoder[5] = get_signals_from_list_that_have_x_matches_with_signal(signals_by_length[5], encoder[6], 5)
    encoder[3] = get_signals_from_list_that_have_x_matches_with_signal(signals_by_length[5], encoder[7], 3)
    encoder[2] = set(signals_by_length[5].pop(0))
    encoder[9] = get_signal_nine(signals_by_length[6], encoder[7], encoder[1], encoder[4])
    encoder[0] = set(signals_by_length[6].pop(0))
    return encoder


def get_decoder(signals):
    encoder = encode_signals(signals)
    return {"".join(sorted(value)): key for key, value in encoder.items()}


def get_signal_nine(signals, signal_seven, signal_one, signal_four):
    # 9 6 -> a is the signal in 7 but not 1, take 4 and add a, 9 is the one that has 5 in common with 4 + a
    signal_a = signal_seven.difference(signal_one)
    signal_four_plus_a = signal_four.union(signal_a)
    return get_signals_from_list_that_have_x_matches_with_signal(signals, signal_four_plus_a, 5)


def get_signals_from_list_that_have_x_matches_with_signal(signals, signal_to_match, number_to_intersect):
    found_signal = None
    for signal in signals:
        if len(signal.intersection(signal_to_match)) == number_to_intersect:
            found_signal = signal
    signals.remove(found_signal)
    return found_signal


def get_signals_by_length(signals):
    signal_lengths = {
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
        7: [],
    }
    for signal in signals:
        signal_lengths[len(signal)].append(set(signal))
    return signal_lengths


def count_instances_of_unique_segments(output_data):
    count = 0
    unique_segment_lengths = [2, 3, 4, 7]
    for display in output_data:
        for digit in display:
            if len(digit) in unique_segment_lengths:
                count += 1
    return count


def solve_a():
    all_signals, all_output = get_input()
    return count_instances_of_unique_segments(all_output)

def solve_b():
    all_signals, all_output = get_input()
    return sum_all_output(all_signals, all_output)


if __name__ == '__main__':
    print(solve_a())
    print(solve_b())
