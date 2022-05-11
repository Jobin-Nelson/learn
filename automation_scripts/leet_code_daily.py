'''This program sets up everything for the daily leetcode problem'''
from pathlib import Path
import subprocess, webbrowser, argparse
from typing import Sequence, Optional
from requests_html import HTMLSession

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="find today's leetcode problem")
    parser.add_argument('-f', '--file', action='store_true', help='create a file if not existing')
    parser.add_argument('-c', '--vscode', action='store_true', help='open file in vscode')
    args = parser.parse_args(argv)

    # api request to get the daily question link
    base_url = 'https://leetcode.com'
    query_url = base_url + '/graphql'
    query = {
      "query": "query questionOfToday {\n\tactiveDailyCodingChallengeQuestion {\n\t\tdate\n\t\tuserStatus\n\t\tlink\n\t\tquestion {\n\t\t\tacRate\n\t\t\tdifficulty\n\t\t\tfreqBar\n\t\t\tfrontendQuestionId: questionFrontendId\n\t\t\tisFavor\n\t\t\tpaidOnly: isPaidOnly\n\t\t\tstatus\n\t\t\ttitle\n\t\t\ttitleSlug\n\t\t\thasVideoSolution\n\t\t\thasSolution\n\t\t\ttopicTags {\n\t\t\t\tname\n\t\t\t\tid\n\t\t\t\tslug\n\t\t\t}\n\t\t}\n\t}\n}\n",
      "operationName": "questionOfToday"
    }

    s = HTMLSession()
    r = s.post(query_url, json=query)
    if r.ok:
        response = r.json()
        daily_qn_link = base_url + response['data']['activeDailyCodingChallengeQuestion']['link']
        webbrowser.open(daily_qn_link)
    else:
        print(f'Received response {r.status_code}')
        print('Aborting program!')
        return 1

    # creating and populating the file if it's not created already
    if args.file:
        filename = Path(daily_qn_link).name + '.py'
        p = Path.home() / 'playground' / 'learn' / 'DSA' / 'competitive_programming' / filename
        if p.exists():
            print('File already exists')
        else:
            with open(p, 'w') as f:
                print(f'Creating file {filename} at {p}')
                f.write(f"'''\nQn:\nLink: {daily_qn_link}\nNotes:\n'''\n")

    # opening the file in vscode
    if args.vscode:
        subprocess.run(['code', str(p)])
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
