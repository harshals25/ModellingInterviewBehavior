
# coding: utf-8

# In[97]:


import numpy as np # linear algebra
import pandas as pd 
import matplotlib.pyplot as plt

interviews = pd.read_csv('Interview - raw.csv')
interviews.head()


# In[98]:


#Original Column Names
interviews.columns


# In[2]:


#interview_df.tail()
#interview_df.drop(1233, inplace=True) #guess maybe the methods require working on a dataframe, but it might already be one,
#especially since we used pandas to read in the file


# In[71]:


interviews.tail()
interviews.drop(1233,inplace=True)


# In[48]:


interviews


# In[99]:


#dropping some unwanted columns
interviews.drop(['Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Name(Cand ID)'], 
                  axis=1, inplace=True)
interviews


# In[100]:


newnames = {
    'Have you obtained the necessary permission to start at the required time':'necessary_permission',
    'Hope there will be no unscheduled meetings':'unscheduled_meetings',
    'Can I Call you three hours before the interview and follow up on your attendance for the interview':'followup_3hours_call',
    'Can I have an alternative number/ desk number. I assure you that I will not trouble you too much':'alternative_number',
    'Have you taken a printout of your updated resume. Have you read the JD and understood the same':'resume_printout_JD',
    'Are you clear with the venue details and the landmark.':'venue_details',
    'Has the call letter been shared':'shared_call_letter',
    'Nature of Skillset':'skillset',
    'Position to be closed':'position'
}
interviews.rename(columns=newnames, inplace=True)


# In[101]:


#New simplified column names
interviews.columns


# In[102]:


#Now cleaning up range of responses in individual fields
interviews.loc[interviews['Observed Attendance']=='NO','Observed Attendance']='No'
interviews.loc[interviews['Observed Attendance']=='No ','Observed Attendance']='No'
interviews.loc[interviews['Observed Attendance']=='no ','Observed Attendance']='No'
interviews.loc[interviews['Observed Attendance']=='no','Observed Attendance']='No'
interviews['Observed Attendance'].value_counts()


# In[103]:


interviews.loc[interviews['Observed Attendance']=='yes','Observed Attendance']='Yes'
interviews['Observed Attendance'].value_counts()


# In[104]:


#confirmed you have to run the previous two lines twice to remove the lowercase 'yes' response
interviews.loc[interviews['Observed Attendance']=='yes ','Observed Attendance']='Yes'
interviews['Observed Attendance'].value_counts()


# In[105]:


interviews['Expected Attendance'].value_counts()
interviews.loc[interviews['Expected Attendance']=='No ','Expected Attendance']='No'
interviews.loc[interviews['Expected Attendance']=='NO','Expected Attendance']='No'
interviews.loc[interviews['Expected Attendance']=='Uncertain','Expected Attendance']='No'
interviews.loc[interviews['Expected Attendance']=='yes','Expected Attendance']='Yes'
interviews['Expected Attendance'].value_counts()


# In[107]:


interviews.loc[interviews['Expected Attendance']=='11:00 AM','Expected Attendance']='Yes'
interviews.loc[interviews['Expected Attendance']=='10.30 Am','Expected Attendance']='Yes'


# In[108]:


interviews['Expected Attendance'].value_counts()


# In[109]:


interviews['Interview Type'].value_counts()


# In[110]:


#changing code to leave 3 interview types:Scheduled, Walk In, and Scheduled Walk In
interviews.loc[interviews['Interview Type']=='Scheduled Walkin','Interview Type']='Scheduled Walk-In'
interviews.loc[interviews['Interview Type']=='Sceduled walkin','Interview Type']='Scheduled Walk-In'
interviews.loc[interviews['Interview Type']=='Scheduled Walk In','Interview Type']='Scheduled Walk-In'
interviews.loc[interviews['Interview Type']=='Walkin ','Interview Type']='Walk-In'
interviews.loc[interviews['Interview Type']=='Walkin','Interview Type']='Walk-In'
interviews['Interview Type'].value_counts()


# In[111]:


interviews['shared_call_letter'].value_counts()


# In[112]:


#multiple blocks like this one didn't work because of double equal sign. So I guess it was comparing them, instead of assigning
interviews.loc[interviews['shared_call_letter']=='yes','shared_call_letter']=='Yes'
interviews.loc[interviews['shared_call_letter']=='Na','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='Not Sure','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='Need To Check','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='Not yet','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='Yet to Check','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='na','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='Havent Checked','shared_call_letter']=='No'
interviews.loc[interviews['shared_call_letter']=='no','shared_call_letter']=='No'
interviews['shared_call_letter'].value_counts()


# In[113]:


interviews.loc[interviews['shared_call_letter']=='yes','shared_call_letter']='Yes'
interviews.loc[interviews['shared_call_letter']=='Na','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Not yet','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Not Sure','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Need To Check','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Yet to Check','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Havent Checked','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='no','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='na','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='Not sure','shared_call_letter']='No/Need to Check'
interviews.loc[interviews['shared_call_letter']=='No','shared_call_letter'] = 'No/Need to Check'


# In[114]:


interviews['shared_call_letter'].value_counts()


# In[45]:


interviews.head()


# In[115]:


interviews['venue_details'].value_counts()


# In[116]:


interviews.loc[interviews['venue_details']=='yes','venue_details']='Yes'
interviews.loc[interviews['venue_details']=='Na','venue_details']='No'
interviews.loc[interviews['venue_details']=='No- I need to check','venue_details']='No'
interviews.loc[interviews['venue_details']=='no','venue_details']='No'
interviews.loc[interviews['venue_details']=='na','venue_details']='No'


# In[117]:


interviews['venue_details'].value_counts()


# In[119]:


interviews['resume_printout_JD'].value_counts()


# In[122]:


interviews.loc[interviews['resume_printout_JD']=='yes','resume_printout_JD']='Yes'
interviews.loc[interviews['resume_printout_JD']=='Na','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='No- Will take it soon','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='No','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='Not yet','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='Not Yet','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='na','resume_printout_JD']='No'
interviews.loc[interviews['resume_printout_JD']=='No- will take it soon','resume_printout_JD']='No'


# In[123]:


interviews['resume_printout_JD'].value_counts()


# In[124]:


interviews['alternative_number'].value_counts()


# In[125]:


interviews.loc[interviews['alternative_number']=='yes','alternative_number']='Yes'
interviews.loc[interviews['alternative_number']=='Na','alternative_number']='No'
interviews.loc[interviews['alternative_number']=='No- I have only thi number','alternative_number']='No'
interviews.loc[interviews['alternative_number']=='No','alternative_number']='No'
interviews.loc[interviews['alternative_number']=='na','alternative_number']='No'
interviews.loc[interviews['alternative_number']=='No I have only thi number','alternative_number']='No'


# In[126]:


interviews['alternative_number'].value_counts()


# In[127]:


interviews['followup_3hours_call'].value_counts()


# In[128]:


interviews.loc[interviews['followup_3hours_call']=='yes','followup_3hours_call']='Yes'
interviews.loc[interviews['followup_3hours_call']=='Na','followup_3hours_call']='No'
interviews.loc[interviews['followup_3hours_call']=='No Dont','followup_3hours_call']='No'
interviews.loc[interviews['followup_3hours_call']=='No','followup_3hours_call']='No'


# In[129]:


interviews['followup_3hours_call'].value_counts()


# In[130]:


interviews['unscheduled_meetings'].value_counts()


# In[131]:


interviews.loc[interviews['unscheduled_meetings']=='yes','unscheduled_meetings']='Yes'
interviews.loc[interviews['unscheduled_meetings']=='Na','unscheduled_meetings']='No'
interviews.loc[interviews['unscheduled_meetings']=='Not Sure','unscheduled_meetings']='No'
interviews.loc[interviews['unscheduled_meetings']=='Not sure','unscheduled_meetings']='No'
interviews.loc[interviews['unscheduled_meetings']=='cant say','unscheduled_meetings']='No'


# In[133]:


interviews.loc[interviews['unscheduled_meetings']=='cant Say','unscheduled_meetings']='No'


# In[134]:


interviews['unscheduled_meetings'].value_counts()


# In[135]:


interviews['necessary_permission'].value_counts()


# In[136]:


interviews.loc[interviews['necessary_permission']=='yes','necessary_permission']='Yes'
interviews.loc[interviews['necessary_permission']=='Na','necessary_permission']='No'
interviews.loc[interviews['necessary_permission']=='Not yet','necessary_permission']='No'
interviews.loc[interviews['necessary_permission']=='Yet to confirm','necessary_permission']='No'
interviews.loc[interviews['necessary_permission']=='NO','necessary_permission']='No'


# In[137]:


interviews['necessary_permission'].value_counts()


# In[77]:


interviews.head()


# In[138]:


interviews['Candidate Job Location'].value_counts()


# In[139]:


interviews['Candidate Current Location'].value_counts()


# In[140]:


interviews.loc[interviews['Candidate Current Location']=='chennai','Candidate Current Location']='Chennai'
interviews.loc[interviews['Candidate Current Location']=='CHENNAI','Candidate Current Location']='Chennai'
interviews.loc[interviews['Candidate Current Location']=='chennai ','Candidate Current Location']='Chennai'


# In[141]:


interviews['Candidate Current Location'].value_counts()


# In[142]:


interviews['Location'].value_counts()


# In[143]:


interviews.loc[interviews['Location']=='chennai','Location']='Chennai'
interviews.loc[interviews['Location']=='CHENNAI','Location']='Chennai'
interviews.loc[interviews['Location']=='chennai ','Location']='Chennai'
interviews.loc[interviews['Location']=='Gurgaonr ','Location']='Gurgaon'


# In[144]:


interviews['Location'].value_counts()


# In[145]:


interviews.loc[interviews['Location']=='Gurgaonr','Location']='Gurgaon'


# In[146]:


interviews['Location'].value_counts()


# In[148]:


#interviews.to_csv('D:\Spring 18\ML\Project/InterviewCleaned.csv)


# In[162]:


interviews['skillset'].value_counts()
#way to messy to deal with. Don't think we should delete it, but don't think it'll be included in the models


# In[163]:


interviews['position'].value_counts()


# In[164]:


#Simplifying position to Routine vs Niche
interviews.loc[interviews['position']=='Dot Net','position']='Niche'
interviews.loc[interviews['position']=='Trade Finance','position']='Niche'
interviews.loc[interviews['position']=='AML','position']='Niche'
interviews.loc[interviews['position']=='Selenium testing','position']='Niche'
interviews.loc[interviews['position']=='Production- Sterile','position']='Niche'


# In[165]:


interviews['position'].value_counts()


# In[160]:


#writing our cleaned dataset to csv
type(interviews)


# In[167]:


#removed indexes from left side of each row
interviews.to_csv('CleanedInterviews - 04.14.18.csv', encoding='utf-8', index=False)

