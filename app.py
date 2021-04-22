# TODO: split sentence at "and"
# TODO: add bridge/interluew between every 4th
# TODO: adjust data innput [1] to capitalize first letter if apporpriate

sample_set = [("penguin", "Turn my head"),
              ("giraffe", "Bend my neck")
              ]


def write_chorus(data):
    lyric_1 = f"Well I am a {data[0]}"
    lyric_2 = f"I can {(data[1]).lower()}"
    lyric_3 = f"Can you {(data[1]).lower()}"
    lyric_4 = "Yes I can!"

    compound_line1 = f"{lyric_1}, {lyric_2}"
    compount_line2 = f"{lyric_3}? {lyric_4}"
    lyric_length1 = len(lyric_1)
    lyric_length2 = len(lyric_3)

    tab_line_1 = ""
    print(tab_line_1)
    print(compound_line1)
    # print([compound_line1, compount_line2])


def write_song(data_set):
    for data in data_set:
        write_chorus(data)


write_chorus(data_set[0])
# write_song(sample_set)
