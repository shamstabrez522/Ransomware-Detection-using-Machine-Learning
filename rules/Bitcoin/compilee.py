import yara
rules=yara.compile('/home/kali/Documents/MLRD-Machine-Learning-Ransomware-Detection/rules/Bitcoin/bitcoin.yara')
print(rules)
