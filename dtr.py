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

    remainder = int(sys.argv[1])
    containers = {}
    resources = Resources()

    no_container = 0

    for amount in resources.mats[sys.argv[2]]:
        containers[amount] = 0
        while remainder - amount >=0:
            containers[amount] += 1
            remainder -= amount
    
    print(remainder)
    print(containers)

    return


if __name__ == "__main__":
    main()

