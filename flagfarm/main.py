import Team
from exploits import *
import Logger
import FlagPoster
from config import *
import time

TEAMS = [
        Team("NPC", NPC_IP)
    ]

EXPLOITS = [
    task0exploit1
]



def endlessLoop(teams: list, exploits: list, flag_poster: FlagPoster):
    log = Logger("Main Loop")
    while True:
        successful_flag_on_iteration = 0
        for team in teams:
            successful_flag_from_team = 0
            log.info("Processing", team.name)
            for exploit in exploits:
                log.info("Task", exploit.__name__)
                new_flags = exploit(team)
                successful_flag_from_team += flag_poster.post_flags(new_flags)
            log.info(f"Got {successful_flag_from_team} flags from {team.name}")
            successful_flag_on_iteration += successful_flag_from_team
        log.info(f"-------------------\n", "Got {successful_flag_from_team} flags from {team.name}\n", "-------------------")
        time.sleep(ROUND_TIMER)
        

        

def main():
    main_logger = Logger("MAIN")
    flag_poster = FlagPoster()

    try:
        endlessLoop(TEAMS, EXPLOITS, flag_poster)
    except InterruptedError:
        main_logger.info("Quitting...")
    finally:
        flag_poster.deserialize()


if __name__ == "__main__":
    main()