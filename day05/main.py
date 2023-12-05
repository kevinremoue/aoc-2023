def get_result_from_stage(seed,stage):
    stage_nb = -1
    right_dest = 0
    print(f"stage {stage} for seed {seed}")
    for substage in stage:
        stage_nb +=1
        destination, source, range = substage.split()
        if int(seed) >= int(source) and int(seed) <= int(source) + int(range):
            print(f"seed {seed} found in substage {stage_nb} returns {int(seed) + (int(destination)-int(source))}")
            return int(seed) + (int(destination)-int(source))
    print(f"seed {seed} not found that stage returns {int(seed)}")
    return seed

        


input = open('day05/input.txt', 'r').read().rstrip().split("\n")
# input = open('day05/test.txt', 'r').read().strip().split("\n")

#Get seeds at first
seeds = input[0].split()
seeds.pop(0)

print(seeds)
print("----------------------")

#Get tables
# tables = open('day05/test.txt', 'r').read().split("\n\n")
tables = open('day05/input.txt', 'r').read().rstrip().split("\n\n")

tables.pop(0) #to delete seeds
stages_dict = {}

#7 categories
for i in range(0,7):
    #get specific tables
    data = tables[i].split("\n")
    # delete title
    data.pop(0)
    stages_dict[i] = data

#We have all stages of conversion in one dict
print(stages_dict)
print("----------------------")

locations = []

for seed in seeds:
    for stage in stages_dict:
        seed = get_result_from_stage(seed,stages_dict[stage])
    locations.append(seed)
    
print(min(locations))