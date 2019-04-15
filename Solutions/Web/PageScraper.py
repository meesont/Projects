# @Author: Thomas Meeson <thomas>
# @Date:   11-04-2019
# @Last modified by:   thomas
# @Last modified time: 15-04-2019
# @License: Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# @Copyright: Copyright(c) 2019 Thomas Meeson


from bs4 import BeautifulSoup as bs
import requests


def get_tags(link):
    r = requests.get(link)

    soup = bs(r.content, "html.parser")
    a_tags = soup.find_all('a')
    return a_tags

if __name__ == '__main__':

    web_link = 'https://www.google.com/'

    tags = get_tags(web_link)
    for i in range(len(tags)):
        print(tags[i])


# Page Scraper - Create an application which connects to a site and pulls out all links, or images, and saves them to a list.
# Optional: Organize the indexed content and don’t allow duplicates. Have it put the results into an easily searchable index file.
