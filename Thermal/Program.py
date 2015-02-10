

import Check_Temperature
import time
import datetime
import Read_Event_Program

on_off_array = Read_Event_Program.Read_Event_Program()
for item in range(len(on_off_array)):
	print on_off_array [item][1] + "," + on_off_array [item][0] + "," +on_off_array [item][2] + "," + on_off_array [item][3]

# Exit "off button" trip that keeps the loop running
ExitCommand = 0

#Set trips for current heating / water
Heating_is_already_on = [False,"0000"]
Water_is_already_on = [False,"0000"]

#For debugging purposes, set a start and finish time automatically
start = int(time.strftime("%H%M"))
end = int((datetime.datetime.now() + datetime.timedelta(minutes=2)).strftime("%H%M")) #int(time.strftime("%H%M"))+6
#print start
#print end

i = 1
while ExitCommand != 1:
	
	#print "Loop_" + str(i) + " " + time.strftime("%a,%H:%M")
	i = i+1
	# get current temperature
	current_temp = Check_Temperature.CheckTemp()
	#print time.strftime("%a,%H:%M") + ",Temp," + str(current_temp) 
	
	on_off_array = Read_Event_Program.Read_Event_Program()
	# Manually Set the on_off times
						#on_off_array = ["Type", "Day", "On", "Off"]
						#on_off_array = ["Water", "Mon", "1348", "1445"], ["Heat", "Mon", "1411", "1502"], ["Heat", "Mon", "1700", "1930"], ["Water", "Mon", "1630", "1730"], \
						#["Water", "Tue", "0921", "0925"], ["Heat", "Tue", "0922", "1025"], ["Heat", "Tue", "1128", "1330"], ["Water", "Tue", "1227", "1429"], \
						#["Water", "Wed", "0845", "0950"], ["Heat", "Wed", "0600", "0730"], ["Heat", "Wed", "0900", "0930"], ["Water", "Wed", "1630", "1730"], \
						#["Water", "Thu", "0700", "0800"], ["Heat", "Thu", "0600", "0730"], ["Heat", "Thu", "1700", "1930"], ["Water", "Thu", "1630", "1730"], \
						#["Water", "Fri", "0700", "0800"], ["Heat", "Fri", "0600", "0730"], ["Heat", "Fri", "1700", "1930"], ["Water", "Fri", "1630", "1730"], \
						#["Water", "Sat", "0700", "0800"], ["Heat", "Sat", "0600", "0730"], ["Heat", "Sat", "1700", "1930"], ["Water", "Sat", "1630", "1730"], \
						#["Water", "Sun", "0700", "0800"], ["Heat", "Sun", "0600", "0730"], ["Heat", "Sun", "1700", "1930"], ["Water", "Sun", "1630", "1730"]
	
						#print on_off_array
		
	j = 0
	# Add a loop to cycle through each row in the table of on/off times
	for row in range(len(on_off_array)):
		
		# Check if the Heating is due to turn on / off
		# Only allow the correct day's items to be checked
		if time.strftime("%a") == (on_off_array [row][1]):
			# If the current time is greater than or equal to the start time then continue
			if int(time.strftime("%H%M")) >= int((on_off_array [row][2])):
				
				
				
				# If the current time is less than or equal to the finish time for that period then continue (we know that the current time is within the on/off "window")
				if int(time.strftime("%H%M")) <= int((on_off_array [row][3])):
				
					
					if on_off_array[row][0] == "Heat" and Heating_is_already_on[0] != True:
						# Turn the Heating on
						print time.strftime("%a,%H:%M") + ",Heating,On"
						#Trip the Heating is currently on trip
						Heating_is_already_on = [True, on_off_array [row][3]]
						
					elif on_off_array[row][0] == "Water" and Water_is_already_on[0] != True:
						#Turn the Water on
						print time.strftime("%a,%H:%M") + ",Water,On"
						#Trip the water is already on trip
						Water_is_already_on = [True, on_off_array [row][3]]
				
				# if the time is greater than the finish time and the line item is water and the water is already on, then turn it off
				#The triple check ensures that it is not turned off by the second/third/fourth... cycle of the day
				elif int(time.strftime("%H%M")) > int(Water_is_already_on[1]) and Water_is_already_on[0] == True:
					Water_is_already_on = [False, "0000"]							
					print time.strftime("%a,%H:%M") + ",Water,Off"
					
				# if the time is greater than the finish time and the line item is Heat and the Heating is already on, then turn it off	
				#The triple check ensures that it is not turned off by the second/third/fourth... cycle of the day
				elif int(time.strftime("%H%M")) > int(Heating_is_already_on[1]) and Heating_is_already_on[0] == True:	
					Heating_is_already_on = [False, "0000"]
					print time.strftime("%a,%H:%M") + ",Heating,Off"
					


		
	  	# Compare the time and the air temperature to assess whether it needs to switch
	  	
	  	# Add off over-ride function trigger
	  		
	  		#Possibly - At Press of Button - Set ExitCommand to 0 then re-lauch self
	  	
	  	# Add +1Hr Function Trigger - Launch timer to trip the switch back...
	  		#Possibly - Add "Temp-Heat"/"Temp-Water" row to on_off_array with order to delete the row after the elaplsed time - Avoids problems if it gets re-set etc...
		
		# compare the time and the tank temperature to assess whether it needs to switch
		
		# Ensure over-ride trip is not triggered (if no more water is required in the period, don't heat any more)
	
		# Write Data to csv files for graphing and calculating warm up / cool-down curves
	
	
	# sleep for 5 minutes -> 300
	time.sleep(60)
	
Loop