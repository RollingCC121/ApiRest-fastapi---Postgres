
CREATE TABLE horario (
  "id_horario" serial PRIMARY KEY,
  "hora_pico" varchar not null,
  "hora_inicio" time not null,
  "hora_fin" time not null
  
);
ALTER TABLE horario ADD CONSTRAINT uk_id_horario UNIQUE ("id_horario");

comment on table horario is 'registro sobre de horarios';
comment on column horario.id_horario is 'primary key de la tabla horario'; 
comment on column horario.hora_pico is 'es hora pico [si/no]';
comment on column horario.hora_inicio is 'hora de inicio)';
comment on column horario.hora_fin is 'hora de finalizacion';


CREATE TABLE cargador (
  "id_cargador" serial PRIMARY KEY,
  "estado" varchar not null
);
alter table cargador add constraint uk_id_cargador unique ("id_cargador");

comment on table cargador is 'registro sobre el cargador';
comment on column cargador.id_cargador is 'primary key de la tabla cargador';
comment on column cargador.estado is 'estado del cargador [ocupado/desocupado]';

CREATE table autobus (
  "id_autobus" serial PRIMARY KEY,
  "estado" varchar not null
);
alter table autobus add constraint uk_id_autobus unique ("id_autobus");

comment on table autobus is 'registro de autobuses ';
comment on column autobus.id_autobus is 'primary key de la tabla autobus';
comment on column autobus.estado is 'estado del autobus [parqueado/cargando/operando]';


CREATE TABLE uso_cargador_bus (
  "id_uso_cargador_bus" serial PRIMARY KEY,
  "horario_fk" int not null,
  "cargador_fk" int not null,
  "autobus_fk" int not null
);
alter table uso_cargador_bus add constraint uk_id_uso_cargador_bus unique ("id_uso_cargador_bus");

comment on table uso_cargador_bus is 'registro del funcionamiento de los cargadores';
comment on column uso_cargador_bus.id_uso_cargador_bus is 'primary key de la tabla uso_cargador_bus';
comment on column uso_cargador_bus.horario_fk is 'clave foranea asociada a la tabla horario';
comment on column uso_cargador_bus.cargador_fk is 'clave foranea asociada a la tabla cargador';
comment on column uso_cargador_bus.autobus_fk is 'clave foranea asociada a la tabla autobus';


ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("horario_fk") REFERENCES horario ("id_horario");

ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("cargador_fk") REFERENCES cargador ("id_cargador");

ALTER TABLE uso_cargador_bus ADD FOREIGN KEY ("autobus_fk") REFERENCES autobus ("id_autobus");


-- Crear un procedimiento almacenado para insertar datos en la tabla autobus
CREATE OR REPLACE FUNCTION insertar_autobus(estado_param VARCHAR) RETURNS VOID AS $$
BEGIN
    INSERT INTO autobus(estado) VALUES(estado_param);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insertar_cargador(estado_param VARCHAR) RETURNS VOID AS $$
BEGIN
    INSERT INTO cargador(estado) VALUES (estado_param);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION insertar_horario(hora_pico_param VARCHAR, hora_inicio_param TIME, hora_fin_param TIME) RETURNS VOID AS $$
BEGIN
    INSERT INTO horario(hora_pico, hora_inicio, hora_fin) VALUES (hora_pico_param, hora_inicio_param, hora_fin_param);
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION insertar_uso_cargador_bus(horario_fk_param INT, cargador_fk_param INT, autobus_fk_param INT) RETURNS VOID AS $$
BEGIN
    INSERT INTO uso_cargador_bus(horario_fk, cargador_fk, autobus_fk) VALUES (horario_fk_param, cargador_fk_param, autobus_fk_param);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION eliminar_autobus_por_id(id_param INT)
RETURNS VOID AS $$
BEGIN
    DELETE FROM "autobus" WHERE id_autobus = id_param;
END;
$$ LANGUAGE plpgsql;


-- Procedimiento para eliminar un registro de la tabla horario
CREATE OR REPLACE PROCEDURE delete_from_horario(id_to_delete INT) AS $$
BEGIN
  DELETE FROM horario WHERE id_horario = id_to_delete;
END;
$$ LANGUAGE plpgsql;

-- Procedimiento para eliminar un registro de la tabla cargador
CREATE OR REPLACE PROCEDURE delete_from_cargador(id_to_delete INT) AS $$
BEGIN
  DELETE FROM cargador WHERE id_cargador = id_to_delete;
END;
$$ LANGUAGE plpgsql;

-- Procedimiento para eliminar un registro de la tabla autobus
CREATE OR REPLACE PROCEDURE delete_from_autobus(id_to_delete INT) AS $$
BEGIN
  DELETE FROM autobus WHERE id_autobus = id_to_delete;
END;
$$ LANGUAGE plpgsql;



-- Procedimiento para eliminar un registro de la tabla uso_cargador_bus
CREATE OR REPLACE PROCEDURE delete_from_uso_cargador_bus(id_to_delete INT) AS $$
BEGIN
  DELETE FROM uso_cargador_bus WHERE id_uso_cargador_bus = id_to_delete;
END;
$$ LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION actualizar_horario(id_horario_param int, nueva_hora_pico varchar, nueva_hora_inicio time, nueva_hora_fin time)
RETURNS void AS $$
BEGIN
  UPDATE horario
  SET hora_pico = nueva_hora_pico, hora_inicio = nueva_hora_inicio, hora_fin = nueva_hora_fin
  WHERE id_horario = id_horario_param;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION actualizar_cargador(id_cargador_param int, nuevo_estado varchar)
RETURNS void AS $$
BEGIN
  UPDATE cargador
  SET estado = nuevo_estado
  WHERE id_cargador = id_cargador_param;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION actualizar_autobus(id_autobus_param int, nuevo_estado varchar)
RETURNS void AS $$
BEGIN
  UPDATE autobus
  SET estado = nuevo_estado
  WHERE id_autobus = id_autobus_param;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION actualizar_uso_cargador_bus(id_uso_cargador_bus_param int, nuevo_horario_fk int, nuevo_cargador_fk int, nuevo_autobus_fk int)
RETURNS void AS $$
BEGIN
  UPDATE uso_cargador_bus
  SET horario_fk = nuevo_horario_fk, cargador_fk = nuevo_cargador_fk, autobus_fk = nuevo_autobus_fk
  WHERE id_uso_cargador_bus = id_uso_cargador_bus_param;
END;
$$ LANGUAGE plpgsql;



-- Crea el procedimiento almacenado
CREATE OR REPLACE FUNCTION informe_utilizacion_cargadores_por_hora() RETURNS TABLE (
    hora_pico varchar,
    hora_inicio time,
    hora_fin time,
    total_cargadores int,
    cargadores_ocupados int
) AS $$
DECLARE
    hora_rec horario%rowtype; -- Variable de tipo registro para el bucle
BEGIN
    -- Itera a través de los horarios
    FOR hora_rec IN SELECT * FROM horario
    LOOP
        -- Obtiene la hora pico, hora de inicio y hora de fin
        hora_pico := hora_rec.hora_pico;
        hora_inicio := hora_rec.hora_inicio;
        hora_fin := hora_rec.hora_fin;
        
        -- Calcula el total de cargadores en ese horario
        SELECT COUNT(*) INTO total_cargadores
        FROM cargador;
        
        -- Calcula la cantidad de cargadores ocupados en ese horario
        SELECT COUNT(*) INTO cargadores_ocupados
        FROM uso_cargador_bus
        WHERE horario_fk = hora_rec.id_horario;
        
        -- Devuelve la fila actual como resultado
        RETURN NEXT;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Ejecuta el procedimiento almacenado
SELECT * FROM informe_utilizacion_cargadores_por_hora();



-- Crea el procedimiento almacenado
CREATE OR REPLACE FUNCTION informe_utilizacion_cargadores_por_hora() RETURNS TABLE (
    hora varchar,
    total_cargadores int,
    cargadores_ocupados int
) AS $$
DECLARE
    hora_rec horario%rowtype; -- Variable de tipo registro para el bucle
BEGIN
    -- Itera a través de los horarios
    FOR hora_rec IN SELECT * FROM horario
    LOOP
        -- Obtiene la hora pico
        hora := hora_rec.hora_pico;
        
        -- Calcula el total de cargadores en ese horario
        SELECT COUNT(*) INTO total_cargadores
        FROM cargador;
        
        -- Calcula la cantidad de cargadores ocupados en ese horario
        SELECT COUNT(*) INTO cargadores_ocupados
        FROM uso_cargador_bus
        WHERE horario_fk = hora_rec.id_horario;
        
        -- Devuelve la fila actual como resultado
        RETURN NEXT;
    END LOOP;
END;
$$ LANGUAGE plpgsql;

-- Ejecuta el procedimiento almacenado
SELECT * FROM informe_utilizacion_cargadores_por_hora();


-- Crea un procedimiento almacenado que genera un informe de utilización de autobuses por hora
CREATE OR REPLACE FUNCTION generar_informe_utilizacion_autobuses()
RETURNS TABLE (
    "Hora" varchar,
    "Hora_Inicio" time,
    "Hora_Fin" time,
    "Autobuses_Utilizados" integer
) AS $$
DECLARE
    row_record RECORD;
BEGIN
    -- Recorre los registros de la tabla "horario"
    FOR row_record IN (SELECT "hora_pico", "hora_inicio", "hora_fin" FROM horario)
    LOOP
        -- Cuenta la cantidad de autobuses utilizados en cada hora
        RETURN QUERY
        SELECT row_record."hora_pico" AS "Hora",
               row_record."hora_inicio" AS "Hora_Inicio",
               row_record."hora_fin" AS "Hora_Fin",
               COUNT(*)::integer AS "Autobuses_Utilizados" -- Convierte el resultado de COUNT(*) a integer
        FROM uso_cargador_bus uc
        JOIN horario h ON uc.horario_fk = h.id_horario
        WHERE h."hora_pico" = row_record."hora_pico"
        GROUP BY row_record."hora_pico", row_record."hora_inicio", row_record."hora_fin";
    END LOOP;
END;
$$ LANGUAGE plpgsql; 


SELECT * FROM generar_informe_utilizacion_autobuses();

