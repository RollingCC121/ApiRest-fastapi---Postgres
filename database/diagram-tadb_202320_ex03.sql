CREATE TABLE "programacion_autobuses" (
  "id_programacion_autobuses" serial PRIMARY KEY,
  "autobus_fk" integer,
  "horario_fk" int
);

CREATE TABLE "cargador" (
  "id_cargador" serial PRIMARY KEY,
  "autobus_fk" varchar
);

CREATE TABLE "horario" (
  "id_horario" serial PRIMARY KEY,
  "hora" time,
  "hora_pico" varchar
);

CREATE TABLE "autobus" (
  "id_autobus" serial PRIMARY KEY,
  "placa" varchar,
  "marca" varchar,
  "ruta" varchar
);

CREATE TABLE "programacion_cargadores" (
  "id_programacion_cargadores" serial PRIMARY KEY,
  "etnia" varchar,
  "horario_fk" int,
  "autobus_fk" int
);

ALTER TABLE "programacion_cargadores" ADD FOREIGN KEY ("horario_fk") REFERENCES "horario" ("id_horario");

ALTER TABLE "programacion_cargadores" ADD FOREIGN KEY ("autobus_fk") REFERENCES "autobus" ("id_autobus");

ALTER TABLE "cargador" ADD FOREIGN KEY ("autobus_fk") REFERENCES "autobus" ("id_autobus");

ALTER TABLE "autobus" ADD FOREIGN KEY ("id_autobus") REFERENCES "programacion_autobuses" ("autobus_fk");

ALTER TABLE "programacion_autobuses" ADD FOREIGN KEY ("horario_fk") REFERENCES "horario" ("id_horario");
