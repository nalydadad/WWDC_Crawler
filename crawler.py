from bs4 import BeautifulSoup
import requests
import sys

def parse_html():
    # type: () -> void
    year = 2022
    if len(sys.argv) > 1:
        year = sys.argv[1]
    year = f"wwdc{year}"
    
    url = "https://developer.apple.com/videos/" + year
    print('Parsing ' + url + ' ...')

    res = requests.get(url)

    # find the section all sessions
    soup = BeautifulSoup(res.text, 'html.parser')
    section = soup.findAll('section', {'class': 'all-content'})

    # parse each data of all sessions
    soup2 = BeautifulSoup(str(section), 'html.parser')
    images = soup2.findAll('img')
    smaller_description = soup2.findAll('p', {'class': 'description'})
    hyper_links = soup2.findAll('a', href=True)

    # write file
    file_handler_title = open('./WWDC'+ year +'_session_title.md', 'w')
    file_handler_content = open('./WWDC'+ year +'_session_content.md', 'w')
    if len(images) == len(smaller_description):
        print('Number of Sessions:' + str(len(images)))
        for index in range(0, len(images), 1):
            # content
            title = '## ' + images[index]['alt']
            description = smaller_description[index].text
            hyperlink = url + hyper_links[index * 2]['href']
            hyperlink1 = '[link](' + hyperlink + ')'
            hyperlink2 = str(index+1) + '. [' + images[index]['alt'] + '](' + hyperlink + ')'

            # file_handler_content
            file_handler_content.write(title)
            file_handler_content.write("\n")
            file_handler_content.write(description)
            file_handler_content.write("\n")
            file_handler_content.write(hyperlink1)
            file_handler_content.write("\n")
            file_handler_content.write("\n")

            # file_handler_title
            file_handler_title.write(hyperlink2)
            file_handler_title.write("\n")

    file_handler_content.close()
    file_handler_title.close()

if __name__ == '__main__':
    parse_html()
