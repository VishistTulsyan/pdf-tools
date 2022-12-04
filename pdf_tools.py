def main():  # this function is for restarting the code so don't f with it

    import pikepdf
    from pdf2docx import Converter
    from docx2pdf import convert
    from glob import glob
    from pikepdf import Pdf

    # code by Vishist Tulsyan & Varun Banka
    def help_command():
        print("Hey, I can do the following :\n"
              "1. REVERSE A PDF\n"
              "2. CONVERT PDF TO DOCX\n"
              "3. CONVERT DOCX TO PDF\n"
              "4. MERGE ALL PDF IN THE FOLDER TO A SINGLE PDF\n"
              "5. SPLIT A SINGLE PDF INTO MULTIPLE PDF\n"
              "6. GENERATE A PASSWORD PROTECTED PDF\n"
            #  "7. ROTATE YOUR PDF\n"
              #   code by Varun Banka & Vishist Tulsyan
              "8. KNOW MORE ABOUT ME")

    help_command()

    user_choice = input("So, What would you like to do today?  ")

    if user_choice == "1" or user_choice == "a" or user_choice == "A":
        old_pdf = pikepdf.Pdf.open(input("ENTER YOUR PDF NAME HERE-"))
        old_pdf.pages.reverse()
        old_pdf.save(input("enter the name you want to give"))

    elif user_choice == "2" or user_choice == "b" or user_choice == "B":
        old_pdf = input("ENTER YOUR PDF NAME HERE-")
        obj = Converter(old_pdf)
        new_doc = input("enter the name")
        obj.convert(new_doc)
        obj.close()

    elif user_choice == "3" or user_choice == "c" or user_choice == "C":
        old_pdf = input("ENTER YOUR DOC NAME HERE-")
        new_doc = input("enter the name")
        convert(old_pdf, new_doc)

    elif user_choice == "4" or user_choice == "d" or user_choice == "D":
        new_pdf = Pdf.new()
        for file in glob("*.pdf"):
            old_pdf = Pdf.open(file)
            new_pdf.pages.extend(old_pdf.pages)
        new_pdf.save(
            input("DONE! NOW ENTER THE NAME YOU WANT THE SAVED FILE BE CALLED"))

    elif user_choice == "5" or user_choice == "e" or user_choice == "E":
        old_pdf = Pdf.open(input("ENTER YOUR DOC NAME HERE-"))
        for n, page_con in enumerate(old_pdf.pages):
            new_pdf = Pdf.new()
            new_pdf.pages.append(page_con)
            name = "split" + str(n) + ".pdf"
            new_pdf.save(name)

    elif user_choice == "6" or user_choice == "f" or user_choice == "F":
        old_pdf = Pdf.open(input("ENTER YOUR DOC NAME HERE-"))
        file = pikepdf.Permissions(extract=False)
        old_pdf.save((input("ENTER NAME OF NEW PDF")), encryption=pikepdf.Encryption(user=input("enter pass"),
                                                                                     owner=input("enter owner"),
                                                                                     allow=file))
 #   elif user_choice == "7" or user_choice == "g" or user_choice == "G":
  #      old_pdf = Pdf.open(input("ENTER YOUR DOC NAME HERE-"))
   #     for pg in old_pdf.pages:
    #        pg.Rotate = 90
     #       old_pdf.save(input("ENTER THE NEW FILE NAME"))

    elif user_choice == "8" or user_choice == "H" or user_choice == "h":
        print("I am a smart pdf editing tool made by Vishist and Varun \n")
        print("In order to know more, head over to the following link: ")
        print("https://github.com/Vishistt/pdf-tools")

    else:
        print("That maybe beyond my abilities at the moment \n")


main()

while True:
    wouldYouLikeToStartAgain = input(
        "Would you like to run this tool again y/n ? \n")
    if wouldYouLikeToStartAgain == "y" or wouldYouLikeToStartAgain == "Y" or wouldYouLikeToStartAgain == "Yes" or wouldYouLikeToStartAgain == "Yep" or wouldYouLikeToStartAgain == "yes" or wouldYouLikeToStartAgain == "yep" or wouldYouLikeToStartAgain == "sure":
        main()
    elif wouldYouLikeToStartAgain == "n" or wouldYouLikeToStartAgain == "N" or wouldYouLikeToStartAgain == "No" or wouldYouLikeToStartAgain == "Nope" or wouldYouLikeToStartAgain == "yes" or wouldYouLikeToStartAgain == "nope" or wouldYouLikeToStartAgain == "nah" or wouldYouLikeToStartAgain == "Nah":
        print("Cool thanks for using the programme")
        break
    else:
        print("That maybe beyond my abilities at the moment")
