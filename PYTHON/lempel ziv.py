def lempel_ziv_compression_fixed(input_string):
    table = []
    dictionary = {}
    address = 1
    i = 0
    while i < len(input_string):
        current_string = input_string[i]
        j = i + 1
        while j < len(input_string) and current_string in dictionary:
            current_string += input_string[j]
            j += 1
        if current_string in dictionary and j == len(input_string):
            code_packet = (dictionary[current_string], '-')
        elif len(current_string) > 1 and current_string[:-1] in dictionary:
            prefix = current_string[:-1]
            new_char = current_string[-1]
            prefix_address = dictionary[prefix]
            code_packet = (prefix_address, new_char)
        else:
            code_packet = (0, current_string)
        table.append({
            "Code Packet": code_packet,
            "Address": address,
            "Content": current_string
        })
        dictionary[current_string] = address
        address += 1
        i += len(current_string)
    return table

input_string = 'abbaabbaababbaaaabaabba'
final_result = lempel_ziv_compression_fixed(input_string)
for entry in final_result:
    print(entry)
