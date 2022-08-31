from Cartoon import Cartoon

if __name__ == "__main__":

    nm = str(input("Enter name:"))
    yr = int(input("Enter year of publishing:"))
    dr = int(input("Enter duration of cartoon(in minutes):"))
    pd = str(input("Enter producer:"))

    cartoon = Cartoon(nm, yr, dr, pd)

    cartoon.show()

    cartoon.set_name()
    cartoon.set_year()
    cartoon.set_duration()
    cartoon.set_producer()

    cartoon.show()