#!/usr/bin/env python

import pyodbc
import mysql.connector
import datetime
now = datetime.datetime.now()
import sys

sys.stdout.write(now.strftime("%Y-%m-%d %H:%M:%S"))
sys.stdout.flush()
print ' [INFO] GSN ticket Job Started'


mssql = pyodbc.connect('DRIVER={SQL Server};SERVER=czchowsint316.prg-dc.dhl.com;DATABASE=HelpDesk;UID=eBoard_ServiceAccount;PWD=flkgje435f835hf90243qgf872u4egw2f9782')

gsntest = mysql.connector.connect(user='bharat', password='bharat',host='2.253.249.189',database='gsntest')

cursor_gsn = gsntest.cursor()

cursor_ms = mssql.cursor()

cursor_ms.execute("select ID, Priority, Emergency, Status, Service, Registered, RegMonthName, ActualStart, ActualFinish, Deadline, Caller, CallerOrganizationSearchCode, CallerCountry, CallerLocationRegion, CallerLocationSearchCode, CallerCRESTCodeHigh, CallerCRESTCodeHighDes, CallerBusinessUnitName, RecoveryManager, ReasonCaused, ToWorkgroup, ToPerson, Description, InTRT, DurationMinutes, DateGenerated, TRT, SourceSystem, InformationUpdate, RowID, Criticality, ImpactedArea, ImpactedBU, PrioritySNC, Urgency, Impact from dbo.EmergencyFlightboard")

cursor_gsn.execute("truncate table t_EFB")

rows = cursor_ms.fetchall()

for row in rows:

    vals = [row.ID, row.Priority, row.Emergency, row.Status, row.Service, row.Registered, row.RegMonthName, row.ActualStart, row.ActualFinish, row.Deadline, row.Caller, row.CallerOrganizationSearchCode, row.CallerCountry, row.CallerLocationRegion, row.CallerLocationSearchCode, row.CallerCRESTCodeHigh, row.CallerCRESTCodeHighDes, row.CallerBusinessUnitName, row.RecoveryManager, row.ReasonCaused, row.ToWorkgroup, row.ToPerson, row.Description, row.InTRT, row.DurationMinutes, row.DateGenerated, row.TRT, row.SourceSystem, row.InformationUpdate, row.RowID, row.Criticality, row.ImpactedArea, row.ImpactedBU, row.PrioritySNC, row.Urgency, row.Impact]

    cursor_gsn.execute(
        "INSERT INTO t_EFB(ID, Priority, Emergency, Status, Service, Registered, RegMonthName, ActualStart, ActualFinish, Deadline, Caller, CallerOrganizationSearchCode, CallerCountry, CallerLocationRegion, CallerLocationSearchCode, CallerCRESTCodeHigh, CallerCRESTCodeHighDes, CallerBusinessUnitName, RecoveryManager, ReasonCaused, ToWorkgroup, ToPerson, Description, InTRT, DurationMinutes, DateGenerated, TRT, SourceSystem, InformationUpdate, RowID, Criticality, ImpactedArea, ImpactedBU, PrioritySNC, Urgency, Impact ) \
        VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        vals)

gsntest.commit()

cursor_gsn.execute("UPDATE t_EFB a, Service_Solution b SET a.solution = b.SOLUTION_NAME WHERE a.Service = b.SERVICE_NAME")

gsntest.commit()

cursor_gsn.close()

now = datetime.datetime.now()

sys.stdout.write(now.strftime("%Y-%m-%d %H:%M:%S"))
sys.stdout.flush()
print ' [INFO] Eboard Job completed'
