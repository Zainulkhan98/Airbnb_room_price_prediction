
most_freq_col = ["bathrooms","host_has_profile_pic","host_identity_verified","neighbourhood","host_since_year","host_since_month","host_since_day"]

most_freq_col_after_split = [] #["last_review_date","last_review_month","last_review_year"]

median_col = ["review_scores_rating"]

mean_col =["bathrooms","bedrooms","beds"]

categorical_col = ["property_type","room_type","bed_type","cancellation_policy","cleaning_fee","city","host_has_profile_pic",
                   "host_identity_verified","instant_bookable","neighbourhood"]

scaling_req_col = ["id"]

feature_eng_req_nlp = ["description","name","thumbnail_url"]


date_col = ["host_since","last_review","first_review"]

good_to_drop_col = ["last_review","first_review","thumbnail_url","name","description",'host_response_rate',"zipcode"] #can improve model(maybe)(way too much missing values)

