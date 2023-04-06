import os

API_ID       = int(os.environ.get("API_ID", "9453727"))
API_HASH     = os.environ.get("API_HASH", "d0525302a9a1d0cd15e187b14217452d")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6073642688:AAEqJewfoPqYlA1vzcPnuUfcPcM57OcvCtA")
SESSION      = os.environ.get("SESSION", "BQCFn48tF0BNicCI8osTVCUWI0QppN9ApOJdT95PrKFlkCgSDCjOi7AqTyVyxYrRlnk8x6bpMUrZ3qADeTQNdZHgEQKOHbcAu2siuSno6CISBSgLLviRZgIfyd6Z3BnexFifFP0DLIx0W20P62Q0swzfQSFa2lSCpAn5U2Jb0ijFhfMRH9NQpbWuAiW2F3YmCW7MmcIYukPXUIKZkpQaZkq3ozljFI1DSLvqG1Zy41HtiE0saJKGwuK2H6nE8x5OQFmFB8NI6WO5Mp4xfR_eVZZ_lXiMQe6y_7apWUP6BPOx8s8_JYrOSlB-Pkwk7wrLK2K8MzvstGO958wXAnLCv5Z0AAAAATIFXYAA")
TIME         = int(os.environ.get("TIME", 1800))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001861187663 -1001655485024").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@imaxfilter.xsqdm6z.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "8080")
