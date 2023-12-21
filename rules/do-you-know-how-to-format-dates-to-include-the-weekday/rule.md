---
type: rule
archivedreason: 
title: Do you know how to format dates to include the weekday?
guid: 11a7a554-2fd9-4dad-a588-a06f7e56c68f
uri: do-you-know-how-to-format-dates-to-include-the-weekday
created: 2009-06-26T10:07:46.0000000Z
authors:
- title: William Yin
  url: https://ssw.com.au/people/william-yin
related: []
redirects: []

---

![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/BadDateFormat.gif) 
Figure: Bad example - using the default Date Format

![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/GoodDateFormat.gif)
Figure: Good example - using the Date Format with 'ddd'

**How do you do this ?** 

<!--endintro-->
 By default, the date type column only have two format options:

![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/DateFormateDateOnly.gif)**Figure: Date Format #1** ![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/DateFormateDateAndTime.gif)**Figure: Date Format #2 
** To add the week day(eg.Wed) you need to: 
1. Select List Settings | Columns |Create column | Calculated (calculation based on other columns)
2. See the columns of this list in the "Insert Column", add the column you want to change format, and custom the code in "Formula" like below:  ![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/CalculatedColumnWithFormulaCode.gif) 
**Figure: Calculated column with Formula code**
3. Change the views of the list to use the new Calculated column (WeekDate) instead of the original date column (Date): ![](/rules/do-you-know-how-to-format-dates-to-include-the-weekday/ReplaceOldDate.gif)**Figure: Replace the old Date column (Date) with new Calculated column (WeekDate It should not be this hard - see [suggestion to the SharePoint team to make date formatting easier](http://www.ssw.com.au/ssw/Standards/BetterSoftwareSuggestions/SharePointTeamServices.aspx#ChangeDateFormatShouldBeEasier).**

