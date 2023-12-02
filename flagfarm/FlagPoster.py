from typing import List
from config import *
import os.path
import json
import requests
import Logger
import time
import re

class FlagPoster:
    def __init__(self):
        self.posted_flags = set()
        self.error_flags = list()
        self.log = Logger("FlagPoster")

    def deserialize(self):
        if os.path.exists("resources/flag.json"):
            with open("resources/flag.json", "w+") as file:
                self.posted_flags = set(json.load(file))

    def serialize(self):
        with open("resources/flag.json", "w+") as file:
            json.dump(self.posted_flags, file)

    def try_to_send_mistakes(self):
        for i, pack in enumerate(self.error_flags):
            self.log.info(f"Trying to send mistakes, pack №{i}")
            self.post_pack_of_flags(pack)

    def post_pack_of_flags(self, flag_pack: List[str]):
        assert len(flag_pack) <= 100, "Flag pack must be less than 100 flags"
        try:
            resp = requests.put(FLAG_POST_URL, headers=HEADER_FOR_POST, data=json.dumps(flag_pack))
            successful_flags = resp.text.count("Flag accepted")
            return (0, successful_flags) # Error code and info
        except Exception as e:
            self.log.error("Flag post error: ", e)
            return (1, 0)

    def post_flags(self, flag_array):
        not_posted_flags = [i for i in flag_array if i not in self.posted_flags and re.match(FLAG_REGEX, i)]

        for flag in not_posted_flags:
            self.posted_flags.add(flag)

        success_flags = 0
        for i in range(0, len(not_posted_flags), MAX_FLAG_PACK_LENGTH):
            current_pack_of_flags = not_posted_flags[i : min(i + MAX_FLAG_PACK_LENGTH, len(not_posted_flags))]
            resp = self.post_pack_of_flags(
                current_pack_of_flags
            )
            success_flags += resp
            if resp[0] == 0:
                self.log.info("Successfully posted. Accepted:", resp[1])
            else:
                self.log.info("Added flags to mistakes")
                self.error_flags.append(current_pack_of_flags)
            time.sleep(FLAG_POST_TIMEOUT)
     
        return success_flags