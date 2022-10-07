#!/usr/bin/env python3

import yaml
def main():
    with open("myYAML.yml", "r") as myf:
        pyyaml= yaml.load(myf, Loader=yaml.FullLoader)
    print(pyyaml)
    
    pyyaml[0]['apps'].append('minecraft')
    print(pyyaml)
    
    with open("myYAML.yml.updated", "w") as myf:
        yaml.dump(pyyaml,myf)

if __name__=="__main__":
    main()
