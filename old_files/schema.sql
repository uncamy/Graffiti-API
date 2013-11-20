create table graff_nyc_data (
       id integer primary key autoincrement,
       incident_address text not null,
       borough text not null,
       date_created text not null,
       status text not null,
       lat  real,
       lon real
);
