# diskmerger
To consolidate info from all the hard drives I have

## Context
1. I have 4 hard drives. With a decade's worth of backups. Lets consolidate this. 
2. To Start - checked that the drives open on Mac and Windows. 
3. What do I want? 
   1. Have 1 folder with all the backups consolidated without any duplicates. 
   2. each backup might have duplicates in itself across the backups it saves.
   3. There are zipped and 7z files with the same info - it would be good to clean these up as well
   4. Check for equality of each file. In case the name is the same. But the file is diff. eg: s01e02
   5. Have some other tools to allow for all images/music in a folder to be routed to a specific location, sorted by type. 
   6. learn python
5. More ideas:
   1. Provide merging of files from diff locations with a particular file type - merge all the 2000000 downloaded images
      a. Provide a choice for which folders - you dont want the travel images merged with all the memes.
   2. 


### Things done so far:
1. Got the list of files from all the drives and checked for duplicates.
2. Logging infra for console logs
3. Detect external drives

### Next Steps:
1. First check directory for duplicates and then check the files - so if the whole folder is the same, delete the folder.
2. Check metadata of the files to see if they are the same name - choose larger file in case of conflict?