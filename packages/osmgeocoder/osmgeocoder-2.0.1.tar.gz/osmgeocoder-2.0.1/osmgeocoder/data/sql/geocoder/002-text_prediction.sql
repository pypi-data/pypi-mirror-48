--
-- Predict text from user input to be used in autocompletion
--
CREATE OR REPLACE FUNCTION public.predict_text(user_input text) RETURNS TABLE (word text, ct int, dist int) AS
$$
    -- find some approximate matches
    SELECT
        word,   -- the word found, probably longer or error corrected
        ct,     -- usage count of the word in the wordlist, words with higher usage counts are to be ranked higher
        str.levenshtein(substr(word, 0, length(user_input) + 1), user_input) AS dist -- levenshtein edit distance
    FROM public.wordlist
    WHERE
        (
           -- search for all variants of double metaphone matches, uses the trigram indices created earlier
           str.dmetaphone_alt(word) % str.dmetaphone_alt(user_input)
        OR str.dmetaphone(word) % str.dmetaphone_alt(user_input)
        OR str.dmetaphone_alt(word) % str.dmetaphone(user_input)
        OR str.dmetaphone(word) % str.dmetaphone(user_input)
        )
        -- we only use words that have an edit distance of at least two characters
        -- so we imply the user makes at most two typos before accepting a predicted word
        AND str.levenshtein(substr(word, 0, length(user_input) + 1), user_input) < 3
    ORDER BY
        dist ASC, -- no typos preferred
        ct DESC,  -- more common words preferred
        length(word) ASC, -- start with the shortest prediction that matches
        word ASC -- finally sort alphabetically
    LIMIT 10 -- only return at most 10 predictions
$$ LANGUAGE 'sql';

-- use like this
-- SELECT * FROM predict_text('Dickenr');
