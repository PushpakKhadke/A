class ApplicationController < ActionController::Base
  def calculator
  end

  def calculate
    @num1 = params[:num1].to_f
    @num2 = params[:num2].to_f
    @operation = params[:operation]

    @result = case @operation
              when 'add'
                @num1 + @num2
              when 'subtract'
                @num1 - @num2
              when 'multiply'
                @num1 * @num2
              when 'divide'
                if @num2 == 0
                  "Cannot divide by zero"
                else
                  @num1 / @num2
                end
              else
                "Invalid operation"
              end

    render :calculator
  end
end
