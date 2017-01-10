import requests

latest_year = str(2014)

query_template_front = "https://api.data.gov/ed/collegescorecard/v1/schools.json?"
query_template_back = "&api_key=jdKiGVbPCeUuUD2PbXbPFaSeJfGkzV0IhP7CGtG3&_fields=id,school.name,school.school_url,school.price_calculator_url,2014.admissions.sat_scores.25th_percentile.critical_reading,2014.admissions.sat_scores.75th_percentile.critical_reading,2014.admissions.sat_scores.25th_percentile.math,2014.admissions.sat_scores.75th_percentile.math,2014.admissions.sat_scores.25th_percentile.writing,2014.admissions.sat_scores.75th_percentile.writing,2014.admissions.admission_rate.overall,2014.cost.attendance.academic_year,2014.cost.net_price.public.by_income_level.0-30000,2014.cost.net_price.public.by_income_level.30001-48000,2014.cost.net_price.public.by_income_level.48001-75000,2014.cost.net_price.public.by_income_level.75001-110000,2014.cost.net_price.public.by_income_level.110001-plus,2014.cost.net_price.private.by_income_level.0-30000,2014.cost.net_price.private.by_income_level.30001-48000,2014.cost.net_price.private.by_income_level.48001-75000,2014.cost.net_price.private.by_income_level.75001-110000,2014.cost.net_price.private.by_income_level.110001-plus,2014.completion.completion_rate_4yr_150nt,2014.completion.title_iv.low_inc.completed_by.4yrs,2014.completion.title_iv.mid_inc.completed_by.4yrs,2014.completion.title_iv.high_inc.completed_by.4yrs,2014.completion.title_iv.low_inc.completed_by.6yrs,2014.completion.title_iv.mid_inc.completed_by.6yrs,2014.completion.title_iv.high_inc.completed_by.6yrs,2014.aid.median_debt.income.30001_75000,2014.aid.median_debt.income.greater_than_75000,2014.aid.median_debt.income.0_30000,2014.student.share_dependent_lowincome.0_300000,2010.earnings.student_count,2014.earnings.6_yrs_after_entry.median,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.10,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.25,2014.student.enrollment.all,2014.student.share_dependent_middleincome.300001_48000,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,school.city,school.state,2014.earnings.10_yrs_after_entry.mean_earnings.lowest_tercile,2014.earnings.10_yrs_after_entry.median,2001.earnings.10_yrs_after_entry.mean_earnings.middle_tercile,2014.earnings.10_yrs_after_entry.mean_earnings.highest_tercile,2014.student.demographics.race_ethnicity.white,2014.student.demographics.race_ethnicity.black,2014.student.demographics.race_ethnicity.hispanic,2014.student.demographics.race_ethnicity.asian,2014.student.demographics.race_ethnicity.aian,2014.student.demographics.race_ethnicity.nhpi,2014.student.demographics.race_ethnicity.two_or_more,2014.student.demographics.race_ethnicity.non_resident_alien,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,&_per_page=20&sort=2014.admissions.sat_scores.midpoint.critical_reading:desc"

print "1) Yes \n2) No"
name_bool = str(raw_input("Do you want to search by school name? "))

if name_bool == "1":


print "1) Yes \n2) No"
SAT_bool = str(raw_input("Do you want an SAT range? "))

if SAT_bool == "1":
    print "SAT within the following..."
    SAT_25th = raw_input("lowest: ")
    SAT_75th = raw_input("highest: ")

    if SAT_25th > SAT_75th:
        temp = SAT_75th
        SAT_75 = SAT_25th
        SAT_25th = temp

    SAT_math_25th = latest_year + ".admissions.sat_scores.25th_percentile.math__range=" + SAT_25th + "..&"
    SAT_math_75th = latest_year + ".admissions.sat_scores.75th_percentile.math__range=.." + SAT_75th + "&"
    SAT_cr_25th = latest_year + ".admissions.sat_scores.25th_percentile.critical_reading__range=" + SAT_25th + "..&"
    SAT_cr_75th = latest_year + ".admissions.sat_scores.75th_percentile.critical_reading__range=.." + SAT_75th + "&"
    SAT_writing_25th = latest_year + ".admissions.sat_scores.25th_percentile.writing__range=" + SAT_25th + "..&"
    SAT_writing_75th = latest_year + ".admissions.sat_scores.75th_percentile.writing__range=.." + SAT_75th + "&"

    SAT_query = SAT_cr_25th + SAT_cr_75th + SAT_math_25th + SAT_math_75th + SAT_writing_25th + SAT_writing_75th

    query_template_front += SAT_query
    print query_template_front

print "1) Yes \n2) No"
admit_rate_bool = str(raw_input("Do you want an Admission Rate? "))

if admit_rate_bool == "1":

    print "Admission Rate: \n(1)>50% \n(2)<50% \n(3)<25% \n(4)<10%"

    admit_rate = raw_input("Enter Admission Rate Range (1 - 4): ")

    admit_rate_query_string = latest_year + ".admissions.admission_rate.overall__range="

    admit_rate_dict = {
        "1": "0.5..",
        "2": "0.25..0.5",
        "3": "0.1..0.25",
        "4": "0.01..0.1",
    }

    query_template_front += admit_rate_query_string + admit_rate_dict[admit_rate] + "&"
    print query_template_front

print "1) Yes \n2) No"
cost_bool = str(raw_input("Do you want to select school based on cost for your income level? "))

if cost_bool == "1":


    print "Income Level: \n(1)<30000 \n(2)<48000 \n(3)<75000 \n(4)<110000 \n(5)>110000"

    income_level = raw_input("Enter Income Level Range (1 - 4): ")

    income_level_dict = {
        "1": "0-30000",
        "2": "30001-48000",
        "3": "48001-75000",
        "4": "75001-110000",
        "5": "110001-plus"
    }

    print "School Type: \n(1)Public \n(2)<Private"

    school_type = raw_input("Enter School Type (1 or 2): ")

    school_type_dict = {
        "1": "public",
        "2": "private"
    }

    max_price = raw_input("Enter Max Price: ")

    cost_query_string = latest_year + ".cost.net_price." + school_type_dict[school_type] + ".by_income_level." + income_level_dict[income_level] + "__range=.." + max_price

    query_template_front += cost_query_string
    print query_template_front


query_template_full = query_template_front + query_template_back
print query_template_full

res = requests.get(query_template_full)
for i in res.json()["results"]:
    print i


# income_range_dict = {
#     "1": "0-30000",
#     "2": "30001-48000",
#     "3": "48001-75000",
#     "4": "75001-110000",
#     "5": "110001-plus"
# }
#
# income_range_query_string = latest_year + ".cost.net_price.public.by_income_level."
# public and private have to be called separately