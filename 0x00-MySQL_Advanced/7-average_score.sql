-- that computes and stores the average score for a student
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT)
BEGIN
    DECLARE average_score FLOAT;
    SELECT AVG(score) INTO average_score FROM projects WHERE user_id = user_id;
    INSERT INTO corrections (user_id, average_score) VALUES(user_id, average_score);
END
$$
DELIMITER ;