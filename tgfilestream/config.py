# tgfilestream - A Telegram bot that can stream Telegram files to users over HTTP.
# Copyright (C) 2019 Tulir Asokan
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import sys
import os

from yarl import URL

try:
    port = 8080
except ValueError:
    port = -1
if not 1 <= port <= 65535:
    print("Please make sure the PORT environment variable is an integer between 1 and 65535")
    sys.exit(1)

try:
    api_id = 1786023
    api_hash = "cd003a0cb8d10148cba0d1b404f2ba2c"
except (KeyError, ValueError):
    print("Please set the TG_API_ID and TG_API_HASH environment variables correctly")
    print("You can get your own API keys at https://my.telegram.org/apps")
    sys.exit(1)

trust_headers = bool(os.environ.get("TRUST_FORWARD_HEADERS"))
host = "0.0.0.0"  #"localhost"
public_url = "https://potatostream.herokuapp.com/"

session_name = "tgfilestream"
bot_token = "1889262909:AAFsEbC0fj7wF101DOkCgk1_OuNGsT_D0GI"

log_config = os.environ.get("LOG_CONFIG")
debug = bool(os.environ.get("DEBUG"))

try:
    # The per-user ongoing request limit
    request_limit = 5
except ValueError:
    print("Please make sure the REQUEST_LIMIT environment variable is an integer")
    sys.exit(1)

try:
    # The per-DC connection limit
    connection_limit = 20
except ValueError:
    print("Please make sure the CONNECTION_LIMIT environment variable is an integer")
    sys.exit(1)
