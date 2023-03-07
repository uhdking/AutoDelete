#=========================================================================
# [AutoDelete - Telegram bot to delete messages after specific time]      
# Copyright (C) 2022 Arunkumar Shibu                       
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#=========================================================================

import os

API_ID       = int(os.environ.get("API_ID", "9453727"))
API_HASH     = os.environ.get("API_HASH", "d0525302a9a1d0cd15e187b14217452d")
BOT_TOKEN    = os.environ.get("BOT_TOKEN", "6073642688:AAG2qupUSyPk9cxJ82gfn5RvAu6WP4-CaYA")
SESSION      = os.environ.get("SESSION", "BQCFn48tF0BNicCI8osTVCUWI0QppN9ApOJdT95PrKFlkCgSDCjOi7AqTyVyxYrRlnk8x6bpMUrZ3qADeTQNdZHgEQKOHbcAu2siuSno6CISBSgLLviRZgIfyd6Z3BnexFifFP0DLIx0W20P62Q0swzfQSFa2lSCpAn5U2Jb0ijFhfMRH9NQpbWuAiW2F3YmCW7MmcIYukPXUIKZkpQaZkq3ozljFI1DSLvqG1Zy41HtiE0saJKGwuK2H6nE8x5OQFmFB8NI6WO5Mp4xfR_eVZZ_lXiMQe6y_7apWUP6BPOx8s8_JYrOSlB-Pkwk7wrLK2K8MzvstGO958wXAnLCv5Z0AAAAATIFXYAA")
TIME         = int(os.environ.get("TIME", 1800))
CHATS        = [int(cht) for cht in os.environ.get("CHATS", "-1001655485024").split()]
WHITE_LIST   = [int(wht) for wht in os.environ.get("WHITE_LIST", "").split()]
BLACK_LIST   = [int(blk) for blk in os.environ.get("BLACK_LIST", "").split()]
DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://uhdprime:uhdprime@cluster0.w3sxrux.mongodb.net/?retryWrites=true&w=majority")
PORT         = os.environ.get("PORT", "80")
