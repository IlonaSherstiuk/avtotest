
def test_staff(web_staff):

        web_staff.open_page()
        web_staff.login()
        web_staff.add_product()
        web_staff.logotype()
        web_staff.search()
        web_staff.go_to_catalog()
        web_staff.respond()
        web_staff.navigata()






        # Закриття браузера
        web_staff.close()





        # page.get_by_label("Номер телефону").fill("666105081")
       # page.pause()

#        page.get_by_role("link", name="button[fdprocessedid]").click()


