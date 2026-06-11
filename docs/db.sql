CREATE TABLE `Untitled` (
	`id`	NUMBER AUTOINCREMENT	NOT NULL,
	`context`	TEXT	NULL,
	`image_link`	TEXT	NULL,
	`created_at`	TEXT	NULL
);

ALTER TABLE `Untitled` ADD CONSTRAINT `PK_UNTITLED` PRIMARY KEY (
	`id`
);

