import sys
class Resources:
    def __init__(self):
        self.mats = {
            "resins":[
            800,
            640,
            480,
            320,
            160,
            80,
            40
        ],
            "metals":[
            1000,
            800,
            600,
            400,
            200,
            100,
            50
        ],
            "ceramics":[
            800,
            640,
            480,
            320,
            160,
            80,
            40
        ],
            "chemicals":[
            600,
            480,
            360,
            240,
            120,
            60,
            30
        ],
            "alloys":[
            1200,
            960,
            720,
            480,
            240,
            120,
            60
        ]
        }


def main():
    containers = {}
    resources = Resources()
    remainder_mats = None
    material_string = None


    if len(sys.argv) == 4:
        remainder_mats = int(sys.argv[2]) - int(sys.argv[1])
        material_string = sys.argv[3]
    
    elif len(sys.argv) == 3:
        remainder_mats = int(sys.argv[1])
        material_string = sys.argv[2]

    else:
        print("Error: Not enough arguments given.")

    
    def loop_resources_and_count_containers(material_string):
        nonlocal remainder_mats

        for amount in resources.mats[material_string]:
                containers[amount] = 0
                while remainder_mats - amount >=0:
                    containers[amount] += 1
                    remainder_mats -= amount
        
        return
    
    loop_resources_and_count_containers(material_string)
    
    print("Remaining Materials: " + str(remainder_mats))
    print(containers)

    return



if __name__ == "__main__":
    main()

