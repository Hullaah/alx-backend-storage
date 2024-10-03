-- creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
    DECLARE average_score DECIMAL;

    SELECT AVG(c.score) INTO average_score
    FROM corrections c
    JOIN users u ON c.user_id = u.id WHERE u.id = user_id;

    UPDATE users SET average_score = average_score WHERE users.id = user_id;
END$$

DELIMITER ;
