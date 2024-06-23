2024-Summer1-EC411-Team-11 Group Project
=========================================
API大全:
- https://github.com/public-apis/public-apis
- https://github.com/TonnyL/Awesome_APIs

API教程:
- python做API接口测试和自动化: https://www.bilibili.com/video/BV1EJ411M7Ln/?spm_id_from=333.337.search-card.all.click&vd_source=84c07544403f8920b4beb27806eb9f70
- 利用API获取开源数据: https://www.bilibili.com/video/BV1Ag411Y7eb/?spm_id_from=333.1007.top_right_bar_window_history.content.click&vd_source=84c07544403f8920b4beb27806eb9f70

Log日志:
- 6/11 成功调动Tripadvisor API。nearby_search是由用户提供经纬度搜索附近10个餐馆，之后回尝试扩大搜索数量。loc_info是用Tripadvisor给餐厅特定的location_id去爬该餐厅的信息，会结合nearby_search一起使用。loc_search是个废案，不考虑，懒得删了。之后的计划是考虑用Uber的API来预估配送费。
- 6/11 把nearby_search和loc_search串联了起来，筛选了目前感觉需要的信息(如name, location_id, address, url, category)。如果需要更多信息可以之后在进行更改。
- 6/12 完善了整个API信息提取的脚本，解决了Tripadvisor API只能提供10个餐厅信息的问题，现在能提供50个不同餐厅的信息。唯一的问题就是运行时间有点长，一次大概需要43秒(就是因为这sb Tripadvisor只能每次提取10个，还是一样的，我只能用两个for loop去提取周边其他餐厅)。之后的计划是开始对前端进行基本开发，先做个登陆界面，插入OAuth，对API key和用户信息进行加密。
- 6/16 做了个登陆界面的基础模板，目前还没有任何功能，可以点击login_signup_page里的index.html进行查看。对Google OAuth2进行了初步测试，我这边应该是出在了VPN的问题上，等待进一步测试。近两天还需要完成的目标有把登陆界面和Google OAuth2连接起来，添加用户数据库，把Tripadvisor API改成以医院为中心对周边的做租房信息进行提取。
- 6/23 把JS，HTML文件与Android Studio进行兼容，在Health_Homes_App里。明天要把SQL数据库完成。

Team Proposal 1: Personalized Food Delivery Recommendations
-----------------------------------------------------------
Overview:
Provide personalized food devlivery recommendations based on user preferences and location. Users can log in via third-party authentication, set up their profile with dietary preferences, and receive tailored food recommendations from local restaurant.
- Public Datasets
	- Tripadvisor: https://developer-tripadvisor.com/home/
	- Uber: https://developer.uber.com/docs/riders/ride-requests/tutorials/api/introduction (可能会用到)
- Code References

Team Proposal 2: Personalized Car Recommendations
-------------------------------------------------
Overview:
Provide personalized car recommendations based on user preferences such as favorite brands and desirable price range. User can log in via third-party authenication, set up their profile their profile with preferences and receive tailored car model suggestions.
- Public Datasets
	- NHTSA Vehicle API: https://vpic.nhtsa.dot.gov/api/?ref=public_apis
	- KBB Vehicle API: http://developer.kbb.com/#!/data/1-Default?ref=public_apis

- Code References

