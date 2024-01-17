from sjvisualizer import Canvas #Helps create the canvas for the video.
from sjvisualizer import DataHandler #Helps import the data from the excel file and interpolate the values for each frame of the video.
from sjvisualizer import Date
from sjvisualizer import StaticText
from sjvisualizer import BarRace
import time
import json


EXCEL_FILE="your/path/towards/data/source"

#Define main function to set the duration, frames per second, font color, and background color, and identify the data frame
def main(duration = 1.0, fps = 60, font_color=(225,225,225), background=(0,0,0)):
    number_of_frames = duration * fps * 60
    df=DataHandler.DataHandler(excel_file=EXCEL_FILE, number_of_frames=number_of_frames).df
    
    # create canvas object
    canvas=Canvas.canvas(bg=background) 

    #Customize colors
    colors_costume={
        "China": (199, 0, 20), # Dark Red
        "India": (255, 103, 31), # Orange
        "Japan": (51, 0, 51), # Brown
        "United States": (10, 49, 97), # Blue
        "Russia": (153, 0, 0), # Red
        "South Korea": (228, 24, 28), # Indigo
        "Germany": (208, 180, 0), # Gold
        "Turkey": (0, 0, 0), # Black
        "France": (96, 115, 115), # Pale light blue
        "Italy": (0, 140, 69), # Green
        "Brazil": (0, 73, 144), # Dark Blue
        "Spain": (241, 191, 0), # Yellow
        "United Kingdom": (192, 192, 192), # Gray
        "Canada": (184, 140, 206), # White
        "Mexico": (0, 99, 65), # Black
        "Poland": (134, 134, 134), # Gray
    }

    # load colors
    #with open("C:/Users/16193/My Drive/Back Up/The Internationalist Group/Political Economy/Planned Economy/China/Steel/Animated Bar Chart/colors.json") as f:
        #colors = json.load(f)


    #Adding the racing bar chart    
    bar_chart=BarRace.bar_race(df=df, canvas=canvas.canvas, costume_colors=colors_costume,
                                x_pos=350, y_pos=200, height=750, colors=colors_costume,
                                 width=1250, shift=150, display_percentages=False, 
                                 display_label=True,back_ground_color=(0,0,0),font_color=font_color)
    canvas.add_sub_plot(bar_chart)

    #Add date
    date = Date.date(canvas=canvas.canvas, df=df, time_indicator="year", width=0, height=65, x_pos=1550, y_pos=850,
                     font_color=font_color)
    canvas.add_sub_plot(date)

    #Add data source
    title = StaticText.static_text(canvas=canvas.canvas, text="Data Source: Worl Steel Association", width=0, height=25, anchor="w",
                                   x_pos=250, y_pos=1000, font_color=font_color)
    canvas.add_sub_plot(title)

    #Add title
    title = StaticText.static_text(canvas=canvas.canvas, text="Steel Production per Country (in tonnages)", width=0, height=70, anchor="c",
                                   x_pos=950, y_pos=50, font_color=font_color)
    canvas.add_sub_plot(title)

    #Add 'made with sjvisualizer'
    title = StaticText.static_text(canvas=canvas.canvas, text="Made with: sjvisualizer", width=0, height=25, anchor="e",
                                   x_pos=1630, y_pos=1020, font_color=font_color)
    canvas.add_sub_plot(title)

    #Play the animation
    canvas.play(fps=fps)


main()


