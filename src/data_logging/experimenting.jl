using Pkg
Pkg.add("DataFrames")
Pkg.add("CSV")
Pkg.add("SQLite")
Pkg.add("DBInterface")
Pkg.add("Tables")
Pkg.add("Plots")

using SQLite
using DBInterface
using DataFrames
using Tables
using Plots

db = SQLite.DB("flight_data.db")

flight_data = DBInterface.execute(db, "SELECT * FROM flight_data")
flights_df = DataFrame(Tables.columntable(flight_data))

sensor_data = DBInterface.execute(db, "SELECT * FROM sensor_data")
sensor_df = DataFrame(Tables.columntable(sensor_data))

event_data = DBInterface.execute(db, "SELECT * FROM events")
events_df = DataFrame(Tables.columntable(event_data))

println("Flight Data Summary:")
println(describe(flights_df))

average_altitude = mean(sensor_df.altitude)
println("Average Altitude: ", average_altitude)

event_count_by_type = combine(groupby(events_df, :event_type), nrow => :count)
println("Event Count by Type:")
println(event_count_by_type)

flight_id_to_plot = 1
flight_sensor_data = filter(row -> row.flight_id == flight_id_to_plot, sensor_df)
plot(flight_sensor_data.timestamp, flight_sensor_data.altitude, legend=false)
xlabel!("Timestamp")
ylabel!("Altitude (meters)")
title!("Altitude Over Time for Flight ID $flight_id_to_plot")
savefig("altitude_over_time_flight_$flight_id_to_plot.png")

SQLite.close(db)
