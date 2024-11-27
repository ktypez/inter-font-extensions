import ufoLib2

def fix(font: ufoLib2.Font):
    # Remap the acutedlbcomb
    font["acutedblcomb"].unicode = int("0x030B", 16)
    
    
# def main():
#     test1 = ufoLib2.Font.open("sources/master_ufo/InterThaiLoopless-Black.ufo")
#     test1 = ufoLib2.Font.open("sources/master_ufo/InterThaiLooped-Black.ufo")

# if __name__ == "__main__":
#     main()