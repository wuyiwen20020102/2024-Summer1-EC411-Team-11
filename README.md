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

