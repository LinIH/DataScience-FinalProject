import requests
import urllib.parse
from bs4 import BeautifulSoup


def count_push(title, link):
    score = 0
    link = link.strip()
    article_link = "https://www.ptt.cc" + link
    #request
    res = requests.get(article_link)
    soup = BeautifulSoup(res.text, 'html.parser')
    #push-tag
    push_tag = soup.select('span.push-tag')
    print(article_link)
    #推 -> +1 / 噓 -> -1
    for a in push_tag:
        if '推' in a.text:
            score += 1
        elif '噓' in a.text:
            score -= 1
        else:
            pass
    #score
    if "好雷" in title:
        # + score
        pass
    elif "負雷" in title:
        score = score * (-1)# - socre

    return score


def load_data(line):
    meta = line.split('\t')
    
    return meta


def main():

    dic = { 'PitchPerfect': 0,              #歌喉讚
            'AlongWiththeGods': 0,          #與神同行
            'Jumanj': 0,                    #野蠻遊戲
            'GreatestShowman': 0,           #大娛樂家
            'StarWars': 0,                  #星際大戰, 星戰, 最後的絕地武士
            'KillingofaSacredDeer': 0,      #聖鹿之死
            'Coco': 0}                      #可可夜總會

    push = {    'PitchPerfect': 0,              #歌喉讚
                'AlongWiththeGods': 0,          #與神同行
                'Jumanj': 0,                    #野蠻遊戲
                'GreatestShowman': 0,           #大娛樂家
                'StarWars': 0,                  #星際大戰, 星戰, 最後的絕地武士
                'KillingofaSacredDeer': 0,      #聖鹿之死
                'Coco': 0}                      #可可夜總會

    f = open('post_list.txt', 'r', encoding = 'utf-8')
    fw = open('record.txt', 'w')
    for line in f:
        meta = load_data(line)
        if "歌喉讚" in meta[2]:
            dic['PitchPerfect'] += 1
            push['PitchPerfect'] += count_push(meta[2], meta[3])
            #print(meta[2], meta[3])
        if "與神同行" in meta[2]:
            dic['AlongWiththeGods'] += 1
            push['AlongWiththeGods'] += count_push(meta[2], meta[3])
        if "野蠻遊戲" in meta[2]:
            dic['Jumanj'] += 1
            push['Jumanj'] += count_push(meta[2], meta[3])
        if "大娛樂家" in meta[2]:
            dic['GreatestShowman'] += 1
            push['GreatestShowman'] += count_push(meta[2], meta[3])
        if "星際大戰" in meta[2] or ("星戰" in meta[2]) or ("最後的絕地武士" in meta[2]):
            dic['StarWars'] += 1
            push['StarWars'] += count_push(meta[2], meta[3])
        if "聖鹿之死" in meta[2]:
            dic['KillingofaSacredDeer'] += 1
            push['KillingofaSacredDeer'] += count_push(meta[2], meta[3])
        if "可可夜總會" in meta[2]:
            dic['Coco'] += 1
            push['Coco'] += count_push(meta[2], meta[3])

    fw.write(str(dic))
    fw.write('\n')
    fw.write(str(push))

    f.close()
    fw.close()

if __name__ == '__main__':
    main()
   