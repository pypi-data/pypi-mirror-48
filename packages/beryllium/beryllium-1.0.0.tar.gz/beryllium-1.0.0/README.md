# Beryllium Package

This is beryllium package. You can use [beryllium](https://guides.github.com/mannuan/beryllium/) to write your lean.

## Beryllium Demo
```python
# -*- coding: utf-8 -*-

from beryllium import Beryllium
import time
from beryllium import FieldList, Field, FieldName, Page, ListCssSelector, Mongodb, NextPageCssSelectorSetup, PageFunc
bery = Beryllium()
bery.driver = bery.get_driver()
bery.fast_get_page("http://search.people.com.cn/cnpeople/news/index.html")
time.sleep(1)
bery.until_send_text_by_css_selector(css_selector="#keyword", text="自闭症")
bery.until_send_enter_by_css_selector(css_selector="#keyword")
time.sleep(2)

fieldlist_shop = FieldList(
    Field(field_name=FieldName.SHOP_NAME, css_selector="li:nth-child(1) > b > a"),
    Field(field_name=FieldName.SHOP_URL, css_selector="li:nth-child(1) > b > a", attr="href"),
    Field(field_name=FieldName.SHOP_TIME, css_selector="li:nth-child(3)", regex=".*([\d]{4}-[\d]{2}-[\d]{2}[ ]+[\d]{2}:[\d]{2}:[\d]{2}).*", replace="\\1"),
)
page_shop = Page(name="shop_page",
                 field_list=fieldlist_shop,
                 list_css_selector=ListCssSelector(list_css_selector="body > div.w980 > div.fr.w800 > ul"),
                 mongodb=Mongodb(db="xinhua", collection="shop"), is_save=True)
bery.until_click_no_next_page_by_css_selector(
    next_page_setup=NextPageCssSelectorSetup(
        page=page_shop,
        css_selector="body > div.w980 > div.fr.w800 > div.show_nav_bar > a:nth-child(10)",
        main_page_func=PageFunc(func=bery.from_page_get_data_list, page=page_shop)
    )
)
```
