# making a circular queeue to store numbers from 1 to 99 and move the pointer to the starting if it hits 99 and count the number of times it hits 0


#ok im an idiot if it says L before the number it means turn left and if it says R it means turn right but we dont care about that for this problem so we will just ignore it
# def import_directions(file_path):
#     with open(file_path, 'r') as file:
#         directions = [int(line.strip().replace("L", "").replace("R", "")) for line in file.readlines()]
#     return directions


# def count_circular_queue_hits(directions):
#     queue = list(range(0, 100))
#     pointer = 0
#     hit_count = 0

#     for move in directions:
#         pointer = (pointer + move) % len(queue)  
#         if queue[pointer] == 0:
#             hit_count += 1

#     return hit_count
# if __name__ == "__main__":
#     directions = import_directions("day1/input.txt")
#     hits = count_circular_queue_hits(directions)
#    print(f"The pointer hit 0 a total of {hits} times.")

def main():
    dial = 50; answer = 0
    with open("day1/input.txt", "r") as file:
        for line in file.readlines():
            if line[0] == "L":
                dial = dial - int(line[1:])
            elif line[0] == "R":
                dial = dial + int(line[1:])
            print(f"rotation of dial in {line[0]} direction by the magnitude of {line[1:]}  ")
            if (dial%100 == 0):
                answer = answer +1
    print(f"answer =  {answer}")
main()