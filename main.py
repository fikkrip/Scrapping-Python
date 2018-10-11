import scrapper

data = []
i = 1

for x in range(5):

    if x>1:

        url = 'https://www.bukalapak.com/c/handphone/hp-smartphone?from=navbar_categories&page='+ str(x) +'&source=navbar'

    elif x==1:

        url = 'https://www.bukalapak.com/c/handphone/hp-smartphone?from=navbar_categories&source=navbar'

    if x>0:
        content = scrapper.get(url)
        articles = content.find_all('article')

        for idx, article in enumerate(articles):

          if idx > 9 and idx <= 39:

              product = article.find_all('div', class_='product-description')
              # name = product[0].find('h3').text
              # name = name[1:-1]

              link = product[0].find('a', class_='product__name')
              link = 'https://www.bukalapak.com' + link['href']

              # print(link)

              # toko = product[0].find('h5', class_='user__name')
              # toko = toko.find('a').text

              detail = scrapper.get(link)
              name = detail.find('h1', class_='c-product-detail__name qa-pd-name').text
              toko = detail.find('a', class_='c-user-identification__name qa-seller-name').text
              jml_feedback = detail.find('a', class_='c-tab__link u-pad-h--2 js-tab-trigger__link qa-pd-feedback-tab').text

              print(name, jml_feedback)

              data.append({
                'name': name,
                'toko': toko,
                'index': i,
                'link': link
              })
              i+=1

user_data = {
  'product':data,
}

# print(user_data)
