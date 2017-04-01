/* demo-app-mf-1 */

TRUNCATE TABLE horses, clients, medications, locations, services;
ALTER SEQUENCE services_id_seq RESTART WITH 1;
ALTER SEQUENCE locations_id_seq RESTART WITH 1;
ALTER SEQUENCE medications_id_seq RESTART WITH 1;
ALTER SEQUENCE horses_id_seq RESTART WITH 1;
ALTER SEQUENCE clients_id_seq RESTART WITH 1;

INSERT INTO clients VALUES
(DEFAULT, 'Peter Scherbel', 'Peter', 'Scherbel', 'Linkenheim', '78654', 'Zorro Strasse 40', '2te Etage', '0721 1562732', '0160 98776512', '', 'p.scherbel@mail.de',
'Privatkonto', 'Peter Scherbel', 'DE5625382836273612', 'SPK62531', 'Konto Oma', 'Juia Scherbel', 'DE2223547382748392', 'SPK62531', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Katrin Scherbel', 'Katrin', 'Scherbel', 'Linkenheim', '78655', 'Zorro Strasse 40', '2te Etage', '0721 1562733', '0160 98776513', '', 'k.scherbel@mail.de',
'Privatkonto', 'Katrin Scherbel', 'DE5625382836273613', 'SPK62533', 'Konto Oma', 'Juia Scherbel', 'DE2223547382748393', 'SPK62532', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Karl Schwarz', 'Karl', 'Schwarz', 'Karlsruhe', '78656', 'Karl Strasse 41', '3te Etage', '0721 1562734', '0160 98776514', '', 'k.schwarz@mail.de',
'Privatkonto', 'Karl Schwarz', 'DE5625382836273614', 'SPK62534', 'Konto Oma', 'Juia Schwarz', 'DE2223547382748394', 'SPK62533', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Horscht Rubert', 'Horscht', 'Rubert', 'Karlsruhe', '78657', 'Karl Strasse 42', '4te Etage', '0721 1562735', '0160 98776515', '', 'h.rubert@mail.de',
'Privatkonto', 'Horscht', 'DE5625382836273615', 'SPK62535', 'Konto Oma', 'Juia Rubert', 'DE2223547382748395', 'SPK62534', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Sigline Gross', 'Sigline', 'Gross', 'Bonn', '78658', 'Gross Strasse 43', '5te Etage', '0721 1562736', '0160 98776516', '', 's.gross@mail.de',
'Privatkonto', 'Sigline Gross', 'DE5625382836273616', 'SPK62536', 'Konto Oma', 'Juia Gross', 'DE2223547382748396', 'SPK62535', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Steffaie Günther', 'Steffaie', 'Günther', 'Baden Baden', '78659', 'Baden Strasse 44', '6te Etage', '0721 1562737', '0160 98776517', '', 's.guenther@mail.de',
'Privatkonto', 'Steffaie Günther', 'DE5625382836273617', 'SPK62537', 'Konto Oma', 'Juia Günther', 'DE2223547382748397', 'SPK62536', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Lui Lausch', 'Lui', 'Lausch', 'Karlsruhe', '78660', 'Krieg Strasse 45', '7te Etage', '0721 1562738', '0160 98776518', '', 'l.lausch@mail.de',
'Privatkonto', 'Lui Lausch', 'DE5625382836273618', 'SPK62538', 'Konto Oma', 'Juia Lausch', 'DE2223547382748398', 'SPK62537', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Marcus Freitag', 'Marcus', 'Freitag', 'Karlsruhe', '78661', 'Krieg Strasse 46', '8te Etage', '0721 1562739', '0160 98776519', '', 'm.freitag@mail.de',
'Privatkonto', 'Marcus Freitag', 'DE5625382836273619', 'SPK62539', 'Konto Oma', 'Juia Freitag', 'DE2223547382748399', 'SPK62538', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel'),
(DEFAULT, 'Nils Freitag', 'Nils', 'Freitag', 'Karlsruhe', '78661', 'Krieg Strasse 46', '8te Etage', '0721 1562740', '0160 98776520', '', 'n.freitag@mail.de',
'Privatkonto', 'Nils Freitag', 'DE5625382836273620', 'SPK62540', 'Konto Oma', 'Juia Freitag', 'DE2223547382748400', 'SPK62539', 0, 0, 0, '', 'Dr Scharf', 'Dr Schnitzel');

INSERT INTO horses VALUES
(DEFAULT, 1, 'Joliscidumiral', '245-09-098', '1968-08-18', 'm', 'weiss', '2015-01-01', NULL, 1),
(DEFAULT, 1, 'Lauser', '245-09-123', '2010-08-18', 'f', 'grau', '2015-01-01', NULL, 1),
(DEFAULT, 1, 'Nelson', '245-33-098', '1999-08-18', 'm', 'braun', '2010-01-01', NULL, 1),
(DEFAULT, 1, 'Capelino', '245-67-100', '1970-01-10', 'm', 'weiss', '2013-01-01', NULL, 1),
(DEFAULT, 1, 'OldMan', '245-00-780', '1936-01-10', 'm', 'weiss', '2010-01-01', '2014-10-31', 0);

INSERT INTO medications VALUES
(DEFAULT, 3, 'Influenza', '2015-03-01', 'Charge-0937'),
(DEFAULT, 3, 'Herpes', '2015-03-05', 'AS3452'),
(DEFAULT, 3, 'Tetanus', '2015-05-05', 'Charge-78457'),
(DEFAULT, 3, 'Entwurmung', '2015-03-01', 'WT5643');

INSERT INTO locations VALUES
(DEFAULT, 3, 'Fensterbox', 'S1-015', 390.00, 'Privatkonto', 'pv001'),
(DEFAULT, 3, 'Koppel', 'k55', 40.00, 'Privatkonto', 'pv001');

INSERT INTO services VALUES
(DEFAULT, 3, 1, 'Beritt Stufe 1', 'Martin', NULL, '2015-12-31', 90.00, 'Privatkonto', 'be006'),
(DEFAULT, 3, 1, 'Führmaschine', '', NULL, '2015-08-31', 50.00, 'Privatkonto', ''),
(DEFAULT, 3, 1, 'Paddockreinigung', '', NULL, NULL, 20.00, 'Privatkonto', ''),
(DEFAULT, 3, 1, 'Unterricht 2x / Woche', 'Karin', '2015-09-01', '2015-09-30', 120.00, 'Konto Oma', 'ur034'),
(DEFAULT, 3, 1, 'Entwurmung', '', NULL, NULL, 10.00, 'Privatkonto', '');
