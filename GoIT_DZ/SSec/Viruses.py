class Malware:
    description = ''
    name = 'unidentified malware'
    signature = '0000'

    def get_description(self):
        return self.description


class Virus(Malware):
    def __init__(self, virus_description, virus_name, virus_signature):
        self.description = virus_description
        self.name = virus_name
        self.signature = virus_signature

        def infect(self, target_system):
            print(f"Oh! I'll create many copies of myself on the "
                  f"{target_system} due to my {self.signature} code.")


class Worm(Malware):
    def __init__(self, worm_description, worm_name, worm_signature):
        self.description = worm_description
        self.name = worm_name
        self.signature = worm_signature

        def infect(self, protocol):
            print(f"Oh! I'll spread myself in your network using {protocol} "
                  f"due to my {self.signature} code.")


class Trojan(Malware):
    def __init__(self, trojan_description, trojan_name, trojan_signature, bait_feature):
        self.description = trojan_description
        self.name = trojan_name
        self.signature = trojan_signature
        self.bait_feature = bait_feature

        def perform_bait_feature(self):
            print(f"You will install me, because I can let you {
                  self.bait_feature}.")


class Antivirus:
    def __init__(self, malware_database):
        self.known_malware = malware_database

    def search(self, code=""):
        for malware in self.known_malware:
            if code.find(malware.signature) != -1:
                print(f"The folowing malware {malware.name} was found.\n"
                      f"Its description is: {malware.description}.\n")


if __name__ == '__main__':
    not_petya = Trojan("Trojan notPetya ransomware encrypting hard drive",
                       "notPetya", "12345667890", "Financial accounting")
    my_doom = Worm("The fastest spreading worm!", "MyDoom", "8754321")
    morris_worm = Worm(
        "The worm, which makes a world take cybersecurity seriously", "Morris worm", "012345")
    chernobyl = Virus(
        "Virus with logic bomb spreading on April, 26", "Chernobyl virus", "789abcdef")

    my_antivirus = Antivirus([not_petya, my_doom, chernobyl, morris_worm])
    my_antivirus.search("0123456789abcdef")
