from bs4 import BeautifulSoup
import requests
import pandas as pd


def get_url(page_no):

    url = 'https://internshala.com/internships/'.format(page_no)
    return url


def gather_information():
    data = {'job_title' :[] ,'company_name' :[] ,'location' :[] ,'start_date' :[] ,'duration' :[] ,'stipend' :[]
            ,'last_date' :[] ,'job_type' :[] ,'Url' :[]}
    for i in range(1 ,17):
        res = requests.get(get_url(i))
        markup = res.content
        soup = BeautifulSoup(markup ,'lxml')
        posts = soup.find_all('div' ,class_='container-fluid individual_internship')

        for i in posts:
            data['job_title'].append(i.find('div' ,class_='heading_4_5 profile').text.strip())
            data['company_name'].append(i.find('a' ,class_='link_display_like_text').text.strip())
            data['location'].append(i.find('a' ,class_='location_link').text)
            data['start_date'].append \
                (i.find('div' ,class_='other_detail_item').find_next(id='start-date-first').text.strip().replace
                    ('Immediately' ,''))
            data['duration'].append(i.find('div' ,class_='item_body' ,id=False).text.strip())
            data['stipend'].append(i.find('span' ,class_='stipend').text)
            data['last_date'].append(i.find('div' ,class_='apply_by').find('div' ,class_='item_body').text)
            data['job_type'].append(i.find('div' ,class_='label_container label_container_desktop').text)
            data['Url'].append('https://internshala.com ' +i.find('div' ,class_='button_container').a['href'])


    # create dataframe
    df = pd.DataFrame(data)
    # save file
    df.to_csv('internship.csv')

if __name__ == "__main__":
    gather_information()