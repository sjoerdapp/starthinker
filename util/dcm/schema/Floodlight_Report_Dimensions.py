###########################################################################
#
#  Copyright 2017 Google Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
###########################################################################

Floodlight_Report_Dimensions_Schema = [
  { "name":"Activity", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Activity_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Activity_Date_Time", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Ad_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Advertiser_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Asset", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Asset_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Asset_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Asset_Orientation", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Audience_Targeted", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Browser_Platform", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_End_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Campaign_Start_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Channel_Mix", "type":"STRING", "mode":"NULLABLE" },
  { "name":"City", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Click_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Click_Through_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Connection_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Conversion_Referrer", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Conversion_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Groups_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Creative_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Creative_Version", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rich_Media_Custom_Event_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Rich_Media_Custom_Event_Path_Summary", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Days_Since_Attributed_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Days_Since_First_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Designated_Market_Area_Dma", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_1_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_2_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_3_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_4_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_Value_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_Value_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Field_Value_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Element_5_Value_Id", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Profile", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Dynamic_Profile_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Floodlight_Attribution_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Configuration", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_1", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_2", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_3", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_4", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_5", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_6", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_7", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_8", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_9", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_10", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_11", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_12", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_13", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_14", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_15", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_16", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_17", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_18", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_19", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_20", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_21", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_22", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_23", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_24", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_25", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_26", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_27", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_28", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_29", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_30", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_31", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_32", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_33", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_34", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_35", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_36", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_37", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_38", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_39", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_40", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_41", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_42", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_43", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_44", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_45", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_46", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_47", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_48", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_49", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_50", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_51", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_52", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_53", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_54", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_55", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_56", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_57", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_58", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_59", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_60", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_61", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_62", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_63", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_64", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_65", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_66", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_67", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_68", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_69", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_70", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_71", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_72", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_73", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_74", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_75", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_76", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_77", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_78", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_79", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_80", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_81", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_82", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_83", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_84", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_85", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_86", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_87", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_88", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_89", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_90", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_91", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_92", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_93", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_94", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_95", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_96", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_97", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_98", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_99", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Floodlight_Variable_100", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Has_Backup_Image", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Counters", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Exits", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Timers", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Dynamic_Impressions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Expansions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Full_Screen_Impressions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Full_Screen_Video_Completions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Full_Screen_Video_Plays", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Full_Screen_Views", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Html5_Impressions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Interactive_Impressions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Manual_Closes", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Companion_Clicks", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Completions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_First_Quartile_Completions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Full_Screen", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Interactions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Midpoints", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Mutes", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Pauses", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Plays", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Progress_Events", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Replays", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Skips", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Stops", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Third_Quartile_Completions", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Unmutes", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Has_Video_Views", "type":"BOOLEAN", "mode":"NULLABLE" },
  { "name":"Hour", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Hours_Since_Attributed_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Hours_Since_First_Interaction", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Impression_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Channel", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Click_Tracker", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Rich_Media", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Static_Image", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Mobile_Video", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Natural_Search", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Paid_Search", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Rich_Media", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Static_Image", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Count_Video", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Interaction_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Mobile_Carrier", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Month", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Country", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Property", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Engine_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Processed_Landing_Page_Query_String", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Natural_Search_Query", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Num_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Operating_System_Version", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Ord_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Package_Roadblock_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Group", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Advertiser", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Advertiser_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Agency", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Agency_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Bid_Strategy", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Bid_Strategy_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Campaign", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account_Category", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Engine_Account_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Ad_Group_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Ad_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Campaign_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_External_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Keyword", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Labels", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Landing_Page_Url", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Paid_Search_Legacy_Keyword_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Paid_Search_Match_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Path_Length", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Path_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_End_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Placement_Pixel_Size", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Placement_Start_Date", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Platform_Type", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rendering_Id", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Video_Length", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Dcm", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Site_Directory", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Site_Id_Site_Directory", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Site_Id_Dcm", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Site_Keyname", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Rich_Media_Standard_Event_Count", "type":"INTEGER", "mode":"NULLABLE" },
  { "name":"Rich_Media_Standard_Event_Path_Summary", "type":"STRING", "mode":"NULLABLE" },
  { "name":"State_Region", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Tran_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"U_Value", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Week", "type":"STRING", "mode":"NULLABLE" },
  { "name":"Zip_Postal_Code", "type":"INTEGER", "mode":"NULLABLE" }
]