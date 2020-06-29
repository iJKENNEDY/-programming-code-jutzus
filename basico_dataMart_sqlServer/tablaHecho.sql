--dimension cliente
MERGE TenebrosaMart.dbo.DimCliente as dim USING
(SELECT z.Descripcion AS Zona, c.Nombre, c.Cliente as IDCliente,
TipoCliente=mt.Descripcion, 
Calificacion = CASE WHEN c.Calificacion ='A' THEN 'Excelente'
		WHEN c.Calificacion ='B' THEN 'Regular'else 'Normal'END
FROM CLIENTE c inner join ZONA z ON c.Zona = z.Zona
inner join MULTITABLA mt ON mt.Valor = c.TipoCliente and mt.Tipo = '01')AS oltp
ON dim.idCliente = oltp.idCliente
WHEN NOT MATCHED THEN
	INSERT (Zona,Categoria,TipoCliente,Cliente, idCliente)
	VALUES (Zona,Calificacion, TipoCliente,Nombre,IdCliente);
GO

--dimension organizacion

MERGE TenebrosaMart.dbo.DimOrganizacion AS Dim USING
(SELECT t.Descripcion AS sucursal, p.Personal AS idPersonal, p.Nombre AS Personal
	FROM PERSONAL p INNER JOIN Tienda t ON p.idTienda= t.idTienda) AS oltp
ON dim.idPersonal = oltp.idPersonal
WHEN NOT MATCHED THEN
	INSERT (Sucursal, Personal, idPersonal)
	VALUES (sucursal, Personal, idPersonal);

-- Dimension TIEMPO

MERGE TenebrosaMart.dbo.DimTiempo AS dim USING
(select DISTINCT Anual =YEAR(D.Fecha),
 Trimestre = DATENAME(yy,D.Fecha)+'-T'+DATENAME(QQ,D.Fecha),
 Mes= DATENAME(mm, D.Fecha), NroMes=DATEPART(mm,D.Fecha),
 DiaSemana=DATENAME(dw,D.Fecha), CONVERT(CHAR(10),d.fecha,101)AS idFecha
 FROM Documento d) as oltp
ON oltp.idfecha = dim.idFecha
WHEN NOT MATCHED THEN
	INSERT (Anual,Trimestre, Mes,NroMes, DiaSemana,idFecha)
	VALUES (Anual, Trimestre, Mes, NroMes,DiaSemana, idFecha);
GO

--- Dimension PRODUCTO
MERGE TenebrosaMart.dbo.DimProducto AS dim USING
 (
SELECT m.Descripcion AS Marca, p.Descripcion as Producto,
p.Producto as idProducto, l.Descripcion AS Linea, pv.RazonSocial
FROM producto p INNER JOIN Marca m ON M.Marca = P.Marca
	INNER JOIN linea l ON l.Linea = m.Linea
	INNER JOIN 	PROVEEDOR pv ON pv.Proveedor = m.Proveedor
) as oltp
ON dim.idProducto = oltp.idProducto
WHEN NOT MATCHED THEN 
INSERT (Proveedor, Linea, Marca, Producto, idProducto)
VALUES (RazonSocial, Linea, Marca, Producto, idProducto);
----------------------

::: --- tabla HECHO ----
INSERT TenebrosaMart.DBO.HechoVentas
(KeyProducto,KeyCliente,KeyOrganizacion,KeyTiempo,UnidadVendido,MontoVendido)
SELECT DP.KeyProducto, dc.KeyCliente, do.KeyOrganizacion, dt.KeyTiempo,
UnidadVendida=SUM(DD.Cantidad),
MontoVenta = SUM(DD.Cantidad * DD.PrecUnit)
FROM detadoc dd INNER JOIN DOCUMENTO d ON D.Documento = DD.Documento AND D.TipoDoc = DD.TipoDoc
	INNER JOIN TenebrosaMart.DBO.DimProducto dp ON DP.idProducto = DD.Producto
	INNER JOIN TenebrosaMart.DBO.DimCliente DC ON dc.idCliente = d.Cliente
	INNER JOIN TenebrosaMart.DBO.DimOrganizacion do ON do.idPersonal = d.Personal
	INNER JOIN TenebrosaMart.DBO.DimTiempo dt ON dt.idFecha = d.Fecha
GROUP BY DP.KeyProducto, dc.KeyCliente, do.KeyOrganizacion, dt.KeyTiempo
  go