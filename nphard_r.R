# Load necessary libraries
library(ggplot2)
library(readr)
data<- read_csv("E:/CMPT/NP hard/time_taken.csv")

# Create the plot
plot <- ggplot(data, aes(x = num_elements, y = time_taken)) +
  geom_line() +
  geom_point() +
  geom_text(aes(label = iteration), vjust = -0.5, hjust = 1.5) +
  labs(title = "Time Taken vs. Number of Elements",
       x = "Number of Elements",
       y = "Time Taken (seconds)") +
  theme_minimal()

# Display the plot
print(plot)

# Save the plot to a file
ggsave("time_taken_plot.png", plot)

