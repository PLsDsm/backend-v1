CREATE TABLE `Untitled` (
	`id`	NUMBER AUTOINCREMENT	NOT NULL,
	`context`	TEXT	NULL,
	`image-link`	TEXT	NULL,
	`created-at`	TEXT	NULL
);

ALTER TABLE `Untitled` ADD CONSTRAINT `PK_UNTITLED` PRIMARY KEY (
	`id`
);

