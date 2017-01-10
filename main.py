# this python file runs the stuff from python
import requests
import json


'''
To be done:
Query methods, SAT scores, cost (income level), admission rate
Do you want an SAT range?
Enter SAT range (each subject):
25th percentile:
75th percentile:

75th percentile > 25th percentile


Admission Rate:
Admission Rate Range:
(1)
(2)
(3)
(4)
>50%
<50%
<25%
<10%
Do you want a cost method?
Enter Income Range from (1) - (4):
(1)
(2)
(3)
(4)

Distance

'''


latest_year = 2014

https://api.data.gov/ed/collegescorecard/v1/schools.json?

+

latest_year.admissions.admission_rate.overall__range=0.01..0.08

latest_year.cost.net_price.public.by_income_level.0-30000
latest_year.cost.net_price.public.by_income_level.30001-48000
latest_year.cost.net_price.public.by_income_level.48001-75000
latest_year.cost.net_price.public.by_income_level.75001-110000
latest_year.cost.net_price.public.by_income_level.110001-plus

latest_year.cost.net_price.private.by_income_level.0-30000
latest_year.cost.net_price.private.by_income_level.30001-48000
latest_year.cost.net_price.private.by_income_level.48001-75000
latest_year.cost.net_price.private.by_income_level.75001-110000
latest_year.cost.net_price.private.by_income_level.110001-plus

latest_year.admissions.sat_scores.25th_percentile.math__range=
latest_year.admissions.sat_scores.75th_percentile.math__range=
latest_year.admissions.sat_scores.25th_percentile.critical_reading__range=
latest_year.admissions.sat_scores.75th_percentile.critical_reading__range=
latest_year.admissions.sat_scores.25th_percentile.writing__range=
latest_year.admissions.sat_scores.75th_percentile.writing__range=

+

&api_key=jdKiGVbPCeUuUD2PbXbPFaSeJfGkzV0IhP7CGtG3&_fields=id,school.name,school.school_url,school.price_calculator_url,2014.admissions.sat_scores.25th_percentile.critical_reading,2014.admissions.sat_scores.75th_percentile.critical_reading,2014.admissions.sat_scores.25th_percentile.math,2014.admissions.sat_scores.75th_percentile.math,2014.admissions.sat_scores.25th_percentile.writing,2014.admissions.sat_scores.75th_percentile.writing,2014.admissions.admission_rate.overall,2014.cost.attendance.academic_year,2014.cost.net_price.public.by_income_level.0-30000,2014.cost.net_price.public.by_income_level.30001-48000,2014.cost.net_price.public.by_income_level.48001-75000,2014.cost.net_price.public.by_income_level.75001-110000,2014.cost.net_price.public.by_income_level.110001-plus,2014.cost.net_price.private.by_income_level.0-30000,2014.cost.net_price.private.by_income_level.30001-48000,2014.cost.net_price.private.by_income_level.48001-75000,2014.cost.net_price.private.by_income_level.75001-110000,2014.cost.net_price.private.by_income_level.110001-plus,2014.completion.completion_rate_4yr_150nt,2014.completion.title_iv.low_inc.completed_by.4yrs,2014.completion.title_iv.mid_inc.completed_by.4yrs,2014.completion.title_iv.high_inc.completed_by.4yrs,2014.completion.title_iv.low_inc.completed_by.6yrs,2014.completion.title_iv.mid_inc.completed_by.6yrs,2014.completion.title_iv.high_inc.completed_by.6yrs,2014.aid.median_debt.income.30001_75000,2014.aid.median_debt.income.greater_than_75000,2014.aid.median_debt.income.0_30000,2014.student.share_dependent_lowincome.0_300000,2010.earnings.student_count,2014.earnings.6_yrs_after_entry.median,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.10,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.25,2014.student.enrollment.all,2014.student.share_dependent_middleincome.300001_48000,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,school.city,school.state,2014.earnings.10_yrs_after_entry.mean_earnings.lowest_tercile,2014.earnings.10_yrs_after_entry.median,2001.earnings.10_yrs_after_entry.mean_earnings.middle_tercile,2014.earnings.10_yrs_after_entry.mean_earnings.highest_tercile,2014.student.demographics.race_ethnicity.white,2014.student.demographics.race_ethnicity.black,2014.student.demographics.race_ethnicity.hispanic,2014.student.demographics.race_ethnicity.asian,2014.student.demographics.race_ethnicity.aian,2014.student.demographics.race_ethnicity.nhpi,2014.student.demographics.race_ethnicity.two_or_more,2014.student.demographics.race_ethnicity.non_resident_alien,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,&_per_page=20&sort=2014.admissions.sat_scores.midpoint.critical_reading:desc



# print json.dumps(i, indent=2)
def getSchoolsByCriteria():
    pass

# for the following provide school json chunk from previous operation
def printSchInfo(school):
    print "Name: %s" % school["school.name"]
    print "Location: %s, %s" % (school["school.city"], school["school.state"])
    print "ID: " + str(school["id"])
    print "Website: %s" % school["school.school_url"]
    print "Net Price Calculator: %s" % school["school.price_calculator_url"]


def printAdmissions(school):
    print "SAT Math: %s - %s" % (school["2014.admissions.sat_scores.25th_percentile.math"], school["2014.admissions.sat_scores.75th_percentile.math"])
    print "SAT Critical Reading: %s - %s" % (school["2014.admissions.sat_scores.25th_percentile.critical_reading"], school["2014.admissions.sat_scores.75th_percentile.critical_reading"])
    print "SAT Writing: %s - %s" % (school["2014.admissions.sat_scores.25th_percentile.writing"], school["2014.admissions.sat_scores.75th_percentile.writing"])
    print "Admission Rate: %s percent" % (school["2014.admissions.admission_rate.overall"]*100)

# 3 income_level
def printCost(school, income_level):
    print "Sticker cost: %s" % school["2014.cost.attendance.academic_year"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.public.by_income_level.0-30000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.public.by_income_level.30001-48000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.public.by_income_level.48001-75000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.public.by_income_level.75001-110000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.public.by_income_level.110001-plus"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.private.by_income_level.0-30000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.private.by_income_level.30001-48000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.private.by_income_level.48001-75000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.private.by_income_level.75001-110000"]
    print "Cost of Attendance: %s" % school["2014.cost.net_price.private.by_income_level.110001-plus"]

# 3 income_level
def printDebt(school, income_level):
    print "Debt: %s" % school["2014.aid.median_debt.income.0_30000"]
    print "Debt: %s" % school["2014.aid.median_debt.income.30001_75000"]
    print "Debt: %s" % school["2014.aid.median_debt.income.greater_than_75000"]

def printDemographics(school):
    print "Percentage Lowest Income: %s" % school["2014.student.share_dependent_lowincome.0_300000"]
    print "Percentage Lower Income: %s" % school["2014.student.share_dependent_middleincome.300001_48000"]
    print "Percentage Middle Income: %s" % school["2014.student.share_dependent_middleincome.48001_75000"]
    print "Percentage Higher Income: %s" % school["2014.student.share_dependent_highincome.75001_110000"]
    print "Percentage Highest Income: %s" % school["2014.student.share_dependent_highincome.110001plus"]
    print "Percentage White: %s" % school["2014.student.demographics.race_ethnicity.white"]
    print "Percentage Black: %s" % school["2014.student.demographics.race_ethnicity.black"]
    print "Percentage Hispanic: %s" % school["2014.student.demographics.race_ethnicity.hispanic"]
    print "Percentage Asian: %s" % school["2014.student.demographics.race_ethnicity.asian"]
    print "Percentage Native American: %s" % school["2014.student.demographics.race_ethnicity.aian"]
    print "Percentage Pcific Islander: %s" % school["2014.student.demographics.race_ethnicity.nhpi"]
    print "Percentage Mixed: %s" % school["2014.student.demographics.race_ethnicity.two_or_more"]
    print "Percentage Foreign: %s" % school["2014.student.demographics.race_ethnicity.non_resident_alien"]

# search by school, SAT range
res = requests.get("https://api.data.gov/ed/collegescorecard/v1/schools.json?2014.admissions.sat_scores.75th_percentile.critical_reading__range=750..&api_key=jdKiGVbPCeUuUD2PbXbPFaSeJfGkzV0IhP7CGtG3&_fields=id,school.name,school.school_url,school.price_calculator_url,2014.admissions.sat_scores.25th_percentile.critical_reading,2014.admissions.sat_scores.75th_percentile.critical_reading,2014.admissions.sat_scores.25th_percentile.math,2014.admissions.sat_scores.75th_percentile.math,2014.admissions.sat_scores.25th_percentile.writing,2014.admissions.sat_scores.75th_percentile.writing,2014.admissions.admission_rate.overall,2014.cost.attendance.academic_year,2014.cost.net_price.public.by_income_level.0-30000,2014.cost.net_price.public.by_income_level.30001-48000,2014.cost.net_price.public.by_income_level.48001-75000,2014.cost.net_price.public.by_income_level.75001-110000,2014.cost.net_price.public.by_income_level.110001-plus,2014.cost.net_price.private.by_income_level.0-30000,2014.cost.net_price.private.by_income_level.30001-48000,2014.cost.net_price.private.by_income_level.48001-75000,2014.cost.net_price.private.by_income_level.75001-110000,2014.cost.net_price.private.by_income_level.110001-plus,2014.completion.completion_rate_4yr_150nt,2014.completion.title_iv.low_inc.completed_by.4yrs,2014.completion.title_iv.mid_inc.completed_by.4yrs,2014.completion.title_iv.high_inc.completed_by.4yrs,2014.completion.title_iv.low_inc.completed_by.6yrs,2014.completion.title_iv.mid_inc.completed_by.6yrs,2014.completion.title_iv.high_inc.completed_by.6yrs,2014.aid.median_debt.income.30001_75000,2014.aid.median_debt.income.greater_than_75000,2014.aid.median_debt.income.0_30000,2014.student.share_dependent_lowincome.0_300000,2010.earnings.student_count,2014.earnings.6_yrs_after_entry.median,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.10,2014.earnings.6_yrs_after_entry.working_not_enrolled.earnings_percentile.25,2014.student.enrollment.all,2014.student.share_dependent_middleincome.300001_48000,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,school.city,school.state,2014.earnings.10_yrs_after_entry.mean_earnings.lowest_tercile,2014.earnings.10_yrs_after_entry.median,2001.earnings.10_yrs_after_entry.mean_earnings.middle_tercile,2014.earnings.10_yrs_after_entry.mean_earnings.highest_tercile,2014.student.demographics.race_ethnicity.white,2014.student.demographics.race_ethnicity.black,2014.student.demographics.race_ethnicity.hispanic,2014.student.demographics.race_ethnicity.asian,2014.student.demographics.race_ethnicity.aian,2014.student.demographics.race_ethnicity.nhpi,2014.student.demographics.race_ethnicity.two_or_more,2014.student.demographics.race_ethnicity.non_resident_alien,2014.student.share_dependent_middleincome.48001_75000,2014.student.share_dependent_highincome.75001_110000,2014.student.share_dependent_highincome.110001plus,&_per_page=20&sort=2014.admissions.sat_scores.midpoint.critical_reading:desc")
for i in res.json()["results"]:
    # prints all info
    # print json.dumps(i, indent=2)
    printSchInfo(i)
    print "\n"
    printAdmissions(i)
    print "\n"
    printCost(i, 0)
    print "\n"
    printDebt(i, 0)
    print "\n"
    printDemographics(i)
    print "\n"
    print "\'\'\'"
    print "\n"
