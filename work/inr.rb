
class P001
    def self.solve(n)
        rv = 0
        (0..n-1).each do |i|
            if i%3 == 0 || i%5 == 0
                rv += i
            end
        end
        puts rv
    end
end

P001.solve(1000)

class P002
    def self.solve(n)
        rv = 0
        a,b,c = 1, 2, 3
        while a < n do
            a = b
            b = c
            c = a+b
            if a % 2 == 0
                rv += a
            end
        end
        puts rv
    end
end

P002.solve(4_000_000)

class P003
    def self.solve(n)
        i = 2
        rv = 0
        while n > 1 do
            while n % i == 0 do
                n /= i
                rv = i
            end
            i += 1
        end
        puts rv
    end
end

P003.solve(600851475143)

class P004
    def self.solve(n)
        rv = 0
        (10**(n-1)..10**n - 1).each do |i|
            (10**(n-1)..10**n - 1).each do |j|
                if (i * j).to_s == (i * j).to_s.reverse && i * j > rv
                    rv = i * j
                end
            end
        end
        puts rv
    end
end

P004.solve(3)

class P005
    def self.gcd(a, b)
        while b != 0 do
            a, b = b, a%b
        end
        return a
    end

    def self.solve(n)
        rv = 1
        for i in 2..n do
            rv = rv * i / gcd(rv, i)
        end
        puts rv
    end
end

P005.solve(20)

class P006
    def self.solve(n)
        rv1 = 0
        rv2 = 0
        (1..n).each do |i|
            rv1 += i
            rv2 += i*i
        end
        puts rv1*rv1 - rv2
    end
end

P006.solve(100)

class P007
    def self.solve(n)
