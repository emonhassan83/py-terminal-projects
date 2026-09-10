from ride import Ride, RideRequest, RideMatching, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

ride_share = RideSharing("my ride")
rider = Rider("rider", "rider@gmail", 1234, "mirpur", 1200)
driver = Driver("driver", 'driver@gmail', 1234, "gulsan")

ride_share.add_rider(rider)
ride_share.add_driver(driver)

print(ride_share)