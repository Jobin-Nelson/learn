#!/usr/bin/env python3
'''This program sets up everything for the daily leetcode problem'''
from datetime import datetime
from pathlib import Path
from typing import Sequence, Optional
import requests
import subprocess, argparse, sys

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="find today's leetcode problem")
    parser.add_argument('-f', '--file', action='store_false', help='do not create a file')
    parser.add_argument('-v', '--vim', action='store_false', help='do not open file in neovim')
    args = parser.parse_args(argv)

    daily_qn_link = get_daily_qn_link()

    filepath = create_file(daily_qn_link, args.file)

    if args.vim:
        subprocess.run(['nvim', str(filepath)])

    return 0

def get_daily_qn_link() -> str:
    base_url = 'https://leetcode.com'
    query_url = base_url + '/graphql'
    query = {
      "query": "query questionOfToday {\n\tactiveDailyCodingChallengeQuestion {\n\t\tdate\n\t\tlink\n\t}\n}\n",
      "operationName": "questionOfToday"
    }

    r = requests.post(query_url, json=query)
    if not r.ok:
        print(f'Received response {r.status_code}')
        print('Aborting program!')
        sys.exit(1)

    response = r.json()
    daily_qn_link = base_url + response['data']['activeDailyCodingChallengeQuestion']['link']
    # subprocess.run(['brave-browser', daily_qn_link], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return daily_qn_link

def create_file(link: str, can_create: bool) -> Path:
    filename = Path(link).name + '.py'
    today = datetime.now()
    p = Path.home() / 'playground' / 'learn' / 'competitive_programming' / f'{today:%Y}' / f'{today:%B}'.lower() / filename
    p.parent.mkdir(exist_ok=True)

    if p.exists():
        print('File already exists')
        return p

    if can_create:
        with open(p, 'w') as f:
            print(f'Creating file {filename} at {p}')
            f.write(f"'''\nCreated Date: {today.strftime('%Y-%m-%d')}\nQn:\nLink: {link}\nNotes:\n'''\ndef main():\n\tpass\n\nif __name__ == '__main__':\n")

    return p

if __name__ == '__main__':
    raise SystemExit(main())
    

