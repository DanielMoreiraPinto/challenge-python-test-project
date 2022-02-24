from src.booking_controller import BookingController


def main():
    booking = input("Defina a reserva >>> ")
    booking_ctrl = BookingController()
    booking_ctrl.assist_booking(booking)
    
if __name__ == '__main__':
    main()